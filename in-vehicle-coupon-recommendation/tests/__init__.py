# Function to check for unreasonable values in numerical features


def check_unreasonable_numerical(feature, lower_bound, upper_bound):
    return data[(data[feature] < lower_bound) | (data[feature] > upper_bound)].shape[0]


# Function to check for unexpected values in categorical features


def check_unexpected_categorical(feature, expected_values):
    return data[~data[feature].isin(expected_values)].shape[0]


# Defining bounds and expected values for each feature

feature_checks = {
    "destination": {"expected_values": ["Work", "No Urgent Place", "Home"]},
    "passanger": {"expected_values": ["Alone", "Friend(s)", "Kid(s)", "Partner"]},
    "weather": {"expected_values": ["Sunny", "Rainy", "Snowy"]},
    "temperature": {"lower_bound": -50, "upper_bound": 130},  # Fahrenheit
    "time": {"expected_values": ["7AM", "10AM", "2PM", "6PM", "10PM"]},
    "coupon": {
        "expected_values": [
            "Coffee House",
            "Bar",
            "Restaurant(20-50)",
            "Carry out & Take away",
            "Restaurant(<20)",
        ]
    },
    "expiration": {"expected_values": ["2h", "1d"]},
    "gender": {"expected_values": ["Female", "Male"]},
    "age": {
        "expected_values": [
            "below21",
            "21",
            "26",
            "31",
            "36",
            "41",
            "46",
            "50plus",
            "56",
        ]
    },
    "maritalStatus": {
        "expected_values": [
            "Unmarried partner",
            "Single",
            "Married partner",
            "Divorced",
            "Widowed",
        ]
    },
    # Skipping 'has_children' as it's binary and less likely to have invalid values
    # Skipping specific checks for 'education', 'occupation', 'income', 'car' due to wide range of possible valid values
    "Bar": {"expected_values": ["never", "less1", "1~3", "4~8", "gt8"]},
    "CoffeeHouse": {"expected_values": ["never", "less1", "1~3", "4~8", "gt8"]},
    "CarryAway": {"expected_values": ["never", "less1", "1~3", "4~8", "gt8"]},
    "RestaurantLessThan20": {
        "expected_values": ["never", "less1", "1~3", "4~8", "gt8"]
    },
    "Restaurant20To50": {"expected_values": ["never", "less1", "1~3", "4~8", "gt8"]},
    # Skipping checks for 'toCoupon_GEQ5min', 'toCoupon_GEQ15min', 'toCoupon_GEQ25min', 'direction_same', 'direction_opp', 'Y' as they are binary/flag features
}


# Performing the checks

invalid_values_summary = {}

for feature, checks in feature_checks.items():
    if "lower_bound" in checks and "upper_bound" in checks:
        invalid_values_summary[feature] = check_unreasonable_numerical(
            feature, checks["lower_bound"], checks["upper_bound"]
        )

    elif "expected_values" in checks:
        invalid_values_summary[feature] = check_unexpected_categorical(
            feature, checks["expected_values"]
        )


invalid_values_summary
