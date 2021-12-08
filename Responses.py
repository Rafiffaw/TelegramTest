def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello'):
        return 'hey'
   
    return "I can't understand you"
