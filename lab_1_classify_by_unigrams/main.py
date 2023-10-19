"""
Lab 1
Language detection
"""


def tokenize(text: str) -> list[str] | None:
    """
    Splits a text into tokens, converts the tokens into lowercase,
    removes punctuation, digits and other symbols
    :param text: a text
    :return: a list of lower-cased tokens without punctuation
    """
    if not isinstance(text, str):
        return None
    tokens = []
    for i in text:
        if i.isalpha():
            tokens += i.lower()
    return tokens


def calculate_frequencies(tokens: list[str] | None) -> dict[str, float] | None:
    """
    Calculates frequencies of given tokens
    :param tokens: a list of tokens
    :return: a dictionary with frequencies
    """
    if not isinstance(tokens, list):
        return None
    for i in tokens:
        if not isinstance(i, str):
            return None
    dictionary = {}
    for i in tokens:
        if i in dictionary:
            dictionary[i] += 1 / len(tokens)
        else:
            dictionary[i] = 1 / len(tokens)
    return dictionary


def create_language_profile(language: str, text: str) -> dict[str, str | dict[str, float]] | None:
    """
    Creates a language profile
    :param language: a language
    :param text: a text
    :return: a dictionary with two keys – name, freq
    """
    if not isinstance(language, str) or not isinstance(text, str):
        return None
    lang_prof = dict({})
    lang_prof['name'] = language
    lang_prof['freq'] = calculate_frequencies(tokenize(text))
    return lang_prof


def calculate_mse(predicted: list, actual: list) -> float | None:
    """
    Calculates mean squared error between predicted and actual values
    :param predicted: a list of predicted values
    :param actual: a list of actual values
    :return: the score
    """
    if (
        not isinstance(predicted, list) or
        not isinstance(actual, list) or
        len(actual) != len(predicted)
    ):
        return None
    sum_squares = 0
    for i, c in enumerate(actual):
        sum_squares += (c - predicted[i]) ** 2
    mse = sum_squares / len(actual)
    return mse


def compare_profiles(
        unknown_profile: dict[str, str | dict[str, float]],
        profile_to_compare: dict[str, str | dict[str, float]]
) -> float | None:
    """
    Compares profiles and calculates the distance using symbols
    :param unknown_profile: a dictionary of an unknown profile
    :param profile_to_compare: a dictionary of a profile to compare the unknown profile to
    :return: the distance between the profiles
    """
    if (
        not isinstance(unknown_profile, dict) or
        not isinstance(profile_to_compare, dict) or
        ('name' or 'freq') not in unknown_profile or
        ('name' or 'freq') not in profile_to_compare
    ):
        return None
    unknown_freq = []
    compare_freq = []
    unknown_tokens = set(unknown_profile['freq'].keys())
    compare_tokens = set(profile_to_compare['freq'].keys())
    tokens = unknown_tokens | compare_tokens
    for token in tokens:
        unknown_freq.append(unknown_profile['freq'].get(token, 0.0))
        compare_freq.append(profile_to_compare['freq'].get(token, 0.0))
    mse = calculate_mse(unknown_freq, compare_freq)
    return mse


def detect_language(
        unknown_profile: dict[str, str | dict[str, float]],
        profile_1: dict[str, str | dict[str, float]],
        profile_2: dict[str, str | dict[str, float]],
) -> str | None:
    """
    Detects the language of an unknown profile
    :param unknown_profile: a dictionary of a profile to determine the language of
    :param profile_1: a dictionary of a known profile
    :param profile_2: a dictionary of a known profile
    :return: a language
    """
    if (
        not isinstance(unknown_profile, dict) or
        not isinstance(profile_1, dict) or
        not isinstance(profile_2, dict)
    ):
        return None
    profile_1_mse = compare_profiles(unknown_profile, profile_1)
    profile_2_mse = compare_profiles(unknown_profile, profile_2)
    if isinstance(profile_1_mse, float) and isinstance(profile_2_mse, float):
        if profile_1_mse < profile_2_mse:
            return str(profile_1['name'])
        if profile_1_mse > profile_2_mse:
            return str(profile_2['name'])
    return str([profile_1['name'], profile_2['name']].sort())


def load_profile(path_to_file: str) -> dict | None:
    """
    Loads a language profile
    :param path_to_file: a path to the language profile
    :return: a dictionary with at least two keys – name, freq
    """


def preprocess_profile(profile: dict) -> dict[str, str | dict] | None:
    """
    Preprocesses profile for a loaded language
    :param profile: a loaded profile
    :return: a dict with a lower-cased loaded profile
    with relative frequencies without unnecessary ngrams
    """


def collect_profiles(paths_to_profiles: list) -> list[dict[str, str | dict[str, float]]] | None:
    """
    Collects profiles for a given path
    :paths_to_profiles: a list of strings to the profiles
    :return: a list of loaded profiles
    """


def detect_language_advanced(unknown_profile: dict[str, str | dict[str, float]],
                             known_profiles: list) -> list | None:
    """
    Detects the language of an unknown profile
    :param unknown_profile: a dictionary of a profile to determine the language of
    :param known_profiles: a list of known profiles
    :return: a sorted list of tuples containing a language and a distance
    """


def print_report(detections: list[tuple[str, float]]) -> None:
    """
    Prints report for detection of language
    :param detections: a list with distances for each available language
    """
