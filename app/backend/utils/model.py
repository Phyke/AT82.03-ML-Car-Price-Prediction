from abc import ABC, abstractmethod
from typing import Literal

import mlflow
import numpy as np
from numpy.typing import NDArray
from sklearn.model_selection import KFold

# np.number is a base class for all integers, floating numbers in numpy
# In Python 3.12, type keyword wass introduced to replace typing.TypeAlias
# read more about this https://docs.astral.sh/ruff/rules/non-pep695-type-alias/
type Vector = NDArray[np.integer | np.floating]
type Matrix = NDArray[np.integer | np.floating]
type Scalar = int | float | np.integer | np.floating

# These are old alternatives
# Vector: TypeAlias = NDArray[np.integer | np.floating]
# Matric: TypeAlias = NDArray[np.integer | np.floating]
# Scalar: TypeAlias = int | float | np.integer | np.floating


class BasePenalty(ABC):
    @abstractmethod
    def __call__(self, theta: Vector) -> Scalar:
        pass

    @abstractmethod
    def derivation(self, theta: Vector) -> Vector:
        pass


class LassoPenalty(BasePenalty):
    def __init__(self, l: Scalar) -> None:
        self.l = l  # lambda value

    # __call__ allows call class as method
    def __call__(self, theta: Vector) -> Scalar:
        return self.l * np.sum(np.abs(theta[1:]))  # do not regularize bias term

    def derivation(self, theta: Vector) -> Vector:
        g = np.zeros_like(theta)
        g[1:] = self.l * np.sign(theta[1:])  # do not regularize bias term
        return g


class RidgePenalty(BasePenalty):
    def __init__(self, l: Scalar) -> None:
        self.l = l

    def __call__(self, theta: Vector) -> Scalar:
        return self.l * np.sum(np.square(theta[1:]))  # do not regularize bias term

    def derivation(self, theta: Vector) -> Vector:
        g = np.zeros_like(theta)
        g[1:] = self.l * 2 * (theta[1:])  # do not regularize bias term
        return g


# class ElasticPenalty(BasePenalty):
#     def __init__(self, l: Scalar = 0.1, l_ratio: Scalar = 0.5) -> None:
#         self.l = l
#         self.l_ratio = l_ratio

#     def __call__(self, theta: Vector) -> Scalar:
#         # The coefficient 1 is to avoid double counting of lambda
#         # Also, do not regularize the bias term but this is handled in Lasso and Ridge
#         # So just pass the full theta
#         l1_contribution = self.l_ratio * LassoPenalty(1)(theta)
#         l2_contribution = (1 - self.l_ratio) * RidgePenalty(1)(theta)
#         return self.l * (l1_contribution + l2_contribution)

#     def derivation(self, theta: Vector) -> Vector:
#         # The coefficient 1 and passing full theta is here as well
#         l1_derivation = self.l_ratio * LassoPenalty(1).derivation(theta)
#         l2_derivation = (1 - self.l_ratio) * RidgePenalty(1).derivation(theta)
#         return self.l * (l1_derivation + l2_derivation)

type TrainMethod = Literal["batch", "stochastic", "mini-batch"]
type WeightInitMethod = Literal["zero", "xavier"]


class LinearRegression:
    cv = KFold(n_splits=3, shuffle=True, random_state=42)

    def __init__(
        self,
        regularization: BasePenalty | None,
        momentum: float,
        train_method: TrainMethod,
        weight_init_method: WeightInitMethod,
        lr: Scalar,
        num_epochs: int,
        batch_size: int | None,
    ) -> None:
        if (train_method in {"batch", "stochastic"}) and batch_size is not None:
            print("Error: Batch size should be None for batch or stochastic gradient descent.")
            return
        if train_method == "mini-batch" and (batch_size is None or batch_size <= 0):
            print("Error: Please provide a valid batch size for mini-batch gradient descent.")
            return
        if regularization is not None and not issubclass(type(regularization), BasePenalty):
            print("Error: regularization should be a subclass of BasePenalty or None.")
            return

        self.regularization = regularization
        self.momentum = momentum
        self.train_method = train_method
        self.weight_init_method = weight_init_method
        self.lr = lr
        self.num_epochs = num_epochs
        self.batch_size = batch_size

    def mse(self, ytrue: Vector, ypred: Vector) -> Scalar:
        return ((ypred - ytrue) ** 2).sum() / ytrue.shape[0]

    def r_squared(self, ytrue: Vector, ypred: Vector) -> Scalar:
        # Formula is 1 - SSres / SStot
        # SSres = Sum of squared residual
        # SStot = Sum of squared totsl (compared to the mean or ybar)
        return 1 - np.sum(np.square(ytrue - ypred)) / np.sum(np.square(ytrue - ytrue.mean()))

    def xavier_weight_init(self, m: int, n: int) -> Vector:
        # Since this method use number of samples to calculate a new uniform range,
        # it requires both m and n to initialize theta (n, )
        upper = 1 / np.sqrt(m)
        lower = -(upper)
        numbers = np.random.rand(n)
        # The scaled output is calculated by
        # 1. streching U(0, 1) into U(0, upper - lower)
        #    with upper - lower = length between lower and upper
        # 2. Add lower to shift all the numbers back to U(lower, upper)
        return lower + numbers * (upper - lower)

    def zero_weight_init(self, n: int) -> Vector:
        return np.zeros(n)

    def weight_init(self, X: Matrix) -> Vector:
        if self.weight_init_method == "zero":
            self.theta = np.zeros(X.shape[1])
        elif self.weight_init_method == "xavier":
            self.theta = self.xavier_weight_init(X.shape[0], X.shape[1])

    def add_intercept(self, X: Matrix) -> Matrix:
        return np.hstack([np.ones((X.shape[0], 1)), X])

    def fit(self, X_train: Matrix, y_train: Vector) -> None:
        # create a list of kfold scores
        self.kfold_scores = []

        # kfold.split in the sklearn.....
        for fold, (train_idx, val_idx) in enumerate(self.cv.split(X_train)):
            # reset val loss at the start of each fold, not outside the fold loop
            self.val_loss_old = np.inf

            X_cross_train = X_train[train_idx]
            y_cross_train = y_train[train_idx]
            X_cross_val = X_train[val_idx]
            y_cross_val = y_train[val_idx]

            # add intercept column to training set as well as validation set
            # so that theta[0] is the bias / intercept
            # X_cross_train has size (m, n+1)
            # X_cross_val has size (m, n+1)
            X_cross_train = self.add_intercept(X_cross_train)
            X_cross_val = self.add_intercept(X_cross_val)

            # define X_cross_train as only a subset of the data
            # how big is this subset?  => mini-batch size ==> 50

            # initialize theta for each fold
            self.weight_init(X_cross_train)
            # This should be vector of same shape as theta
            # but initialized to zero as it will broadcasted anyway
            self.prev_step = 0  # for momentum

            # one epoch will exhaust the WHOLE training set
            with mlflow.start_run(run_name=f"Fold-{fold}", nested=True):
                for epoch in range(self.num_epochs):
                    # with replacement or no replacement
                    # with replacement means just randomize
                    # with no replacement means 0:50, 51:100, 101:150, ......300:323
                    # shuffle your index
                    # https://docs.astral.sh/ruff/rules/numpy-legacy-random/
                    perm = np.random.permutation(X_cross_train.shape[0])

                    X_cross_train = X_cross_train[perm]
                    y_cross_train = y_cross_train[perm]

                    if self.train_method == "stochastic":
                        for batch_idx in range(X_cross_train.shape[0]):
                            # (11,) ==> (1, 11) ==> (m, n)
                            X_method_train = X_cross_train[batch_idx].reshape(1, -1)
                            y_method_train = y_cross_train[batch_idx]
                            train_loss = self._train(X_method_train, y_method_train)
                    elif self.train_method == "mini-batch":
                        for batch_idx in range(0, X_cross_train.shape[0], self.batch_size):
                            # batch_idx = 0, 50, 100, 150
                            X_method_train = X_cross_train[batch_idx : batch_idx + self.batch_size, :]
                            y_method_train = y_cross_train[batch_idx : batch_idx + self.batch_size]
                            train_loss = self._train(X_method_train, y_method_train)
                    elif self.train_method == "batch":
                        X_method_train = X_cross_train
                        y_method_train = y_cross_train
                        train_loss = self._train(X_method_train, y_method_train)
                    else:
                        print("Error: Please select correct training method.")
                        return

                    mlflow.log_metric(key="train_loss", value=train_loss, step=epoch)

                    yhat_val = self.predict(X_cross_val, add_intercept=False)
                    val_loss_new = self.mse(y_cross_val, yhat_val)
                    mlflow.log_metric(key="val_loss", value=val_loss_new, step=epoch)

                    # early stopping
                    if np.allclose(val_loss_new, self.val_loss_old):
                        break
                    self.val_loss_old = val_loss_new

                self.kfold_scores.append(val_loss_new)
                print(f"Fold {fold}: {val_loss_new}")

    def _train(self, X: Matrix, y: Vector) -> Scalar:
        yhat = self.predict(X, add_intercept=False)
        m = X.shape[0]
        grad_loss = (2 / m) * X.T @ (yhat - y)
        if self.regularization is not None:  # noqa: SIM108
            grad_penalty = self.regularization.derivation(self.theta) / m
        else:
            grad_penalty = 0
        grad = grad_loss + grad_penalty
        step = self.lr * grad
        # If momentum is 0, second term is 0, so no momentum
        self.theta = self.theta - step + self.momentum * self.prev_step
        self.prev_step = step

        return self.mse(y, yhat)

    def predict(self, X: Matrix, *, add_intercept: bool = True) -> Vector:
        if add_intercept:
            X = self.add_intercept(X)
        return X @ self.theta  # ===>(m, n) @ (n, )

    def _coef(self) -> Vector:
        return self.theta[1:]  # remind that theta is (w0, w1, w2, w3, w4.....wn)
        # w0 is the bias or the intercept
        # w1....wn are the weights / coefficients / theta

    def _bias(self) -> Scalar:
        return self.theta[0]


class Lasso(LinearRegression):
    def __init__(
        self,
        l: Scalar,
        momentum: float,
        train_method: TrainMethod,
        weight_init_method: WeightInitMethod,
        lr: Scalar,
        num_epochs: int,
        batch_size: int | None,
    ) -> None:
        super().__init__(
            regularization=LassoPenalty(l),
            momentum=momentum,
            train_method=train_method,
            weight_init_method=weight_init_method,
            lr=lr,
            num_epochs=num_epochs,
            batch_size=batch_size,
        )


class Ridge(LinearRegression):
    def __init__(
        self,
        l: Scalar,
        momentum: float,
        train_method: TrainMethod,
        weight_init_method: WeightInitMethod,
        lr: Scalar,
        num_epochs: int,
        batch_size: int | None,
    ) -> None:
        super().__init__(
            regularization=RidgePenalty(l),
            momentum=momentum,
            train_method=train_method,
            weight_init_method=weight_init_method,
            lr=lr,
            num_epochs=num_epochs,
            batch_size=batch_size,
        )


# class ElasticNet(LinearRegression):
#     def __init__(
#         self,
#         l: Scalar,
#         l_ratio: Scalar,
#         momentum: float,
#         train_method: TrainMethod,
#         weight_init_method: WeightInitMethod,
#         lr: Scalar,
#         num_epochs: int,
#         batch_size: int | None,
#     ) -> None:
#         super().__init__(
#             regularization=ElasticPenalty(l, l_ratio),
#             momentum=momentum,
#             train_method=train_method,
#             weight_init_method=weight_init_method,
#             lr=lr,
#             num_epochs=num_epochs,
#             batch_size=batch_size,
#         )
