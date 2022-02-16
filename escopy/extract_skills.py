import pandas as pd
def detect_skills(text, model, nlp, return_dict=False, debug=False):
    """
    Uses a spacy phrase matcher to detect skills
    Args:
        text (str): Text in which to detect skills; note that text should be preprocessed using clean_text() function
        model (dict): Dictionary with the spacy mather ('matcher'), surface
            forms dataframe ('surface_forms'), model name ('name') and spacy language
            model parameters for reference ('nlp')
        return_dict (bool): If True, outputs will be in a dict format
        debug (bool): If True, returns additional data associated with the surface forms
    Returns:
        (pandas.DataFrame or dict): Dataframe or dictionary with the detected surface forms, skills entities and their clusters
    """
    doc = nlp(text)
    matches = model["matcher"](doc)
    detected_forms = [str(doc[match[1] : match[2]]) for match in matches]
    rows = model["surface_forms"].surface_form.isin(detected_forms)
    results_dataframe = (model["surface_forms"][rows]).copy()
    if not debug: 
       
        columns = [
            "is_predicted_OK",
            "surface_form",
            "surface_form_type",
            "preferred_label",
            "entity",
            "predicted_q",
            "cluster_0",
            "cluster_1",
            "cluster_2",
            "label_cluster_0",
            "label_cluster_1",
            "label_cluster_2",
            "manual_OK",
        ]
        results_dataframe = (
            results_dataframe[columns]
            .sort_values("predicted_q")
            .query("is_predicted_OK==1 | manual_OK==1")
            .sort_values("surface_form_type", ascending=False)
            .drop("is_predicted_OK", axis=1)
            .drop("manual_OK", axis=1)
        )

    if not return_dict:
        return results_dataframe

    # Replace pandas/numpy null values with None, for internal consistency
    data = results_dataframe.to_dict("records")
    data = [{k: (None if pd.isnull(v) else v) for k, v in row.items()} for row in data]
    return data