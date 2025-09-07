import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler


def get_preprocessor() -> ColumnTransformer:
    # Define transformers for each feature group
    brand_le = (
        "brand_le",
        Pipeline(
            [
                # Pre-imputer for handling missing values before encoding
                ("pre_imputer", SimpleImputer(strategy="most_frequent")),
                ("encoder", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=np.nan)),
                ("post_imputer", SimpleImputer(strategy="most_frequent")),
                # Post-imputer for handling any NaN introduced by unknown categories during encoding
                # So the pipeline is robust to unseen categories in production data
                # This won't happen if frontend limits the choices to existing categories only
                # But it's better to be safe than sorry
            ],
        ),
        ["brand"],
    )

    fuel_le = (
        "fuel_le",
        Pipeline(
            [
                ("pre_imputer", SimpleImputer(strategy="most_frequent")),
                ("encoder", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=np.nan)),
                ("post_imputer", SimpleImputer(strategy="most_frequent")),
            ],
        ),
        ["fuel"],
    )

    transmission_le = (
        "transmission_le",
        Pipeline(
            [
                ("pre_imputer", SimpleImputer(strategy="most_frequent")),
                ("encoder", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=np.nan)),
                ("post_imputer", SimpleImputer(strategy="most_frequent")),
            ],
        ),
        ["transmission"],
    )

    owner_le = (
        "owner_le",
        Pipeline(
            [
                ("pre_imputer", SimpleImputer(strategy="most_frequent")),
                (
                    "encoder",
                    OrdinalEncoder(
                        categories=[
                            [
                                "First Owner",
                                "Second Owner",
                                "Third Owner",
                                "Fourth & Above Owner",
                            ],
                        ],
                        handle_unknown="use_encoded_value",
                        unknown_value=np.nan,
                    ),
                ),
                ("post_imputer", SimpleImputer(strategy="most_frequent")),
            ],
        ),
        ["owner"],
    )

    seller_type_ohe = (
        "seller_type_ohe",
        Pipeline(
            [
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("encoder", OneHotEncoder(sparse_output=False, drop="first", handle_unknown="ignore")),
            ],
        ),
        ["seller_type"],
    )

    num_scaler = (
        "num_scaler",
        Pipeline(
            [
                (
                    "imputer",
                    ColumnTransformer(
                        transformers=[
                            ("year_imputer", SimpleImputer(strategy="median"), ["year"]),
                            ("km_imputer", SimpleImputer(strategy="median"), ["km_driven"]),
                            ("mileage_imputer", SimpleImputer(strategy="mean"), ["mileage"]),
                            ("engine_imputer", SimpleImputer(strategy="median"), ["engine"]),
                            ("max_power_imputer", SimpleImputer(strategy="median"), ["max_power"]),
                            ("seats_imputer", SimpleImputer(strategy="most_frequent"), ["seats"]),
                        ],
                        remainder="passthrough",
                    ),
                ),
                ("scaler", StandardScaler()),
            ],
        ),
        ["year", "km_driven", "mileage", "engine", "max_power", "seats"],
    )

    # Combine all transformers into the ColumnTransformer
    return ColumnTransformer(
        transformers=[
            brand_le,
            fuel_le,
            transmission_le,
            owner_le,
            seller_type_ohe,
            num_scaler,
        ],
        remainder="passthrough",
        verbose_feature_names_out=True,
    )
