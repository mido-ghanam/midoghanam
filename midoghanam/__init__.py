
def get_preferred_sentence(preferred_language, ar_sentence, en_sentence):
  if not all([preferred_language, ar_sentence, en_sentence]):
    print("Please provide all the required parameters.")
  if str(preferred_language) == "ar":
    return ar_sentence
  elif str(preferred_language) == "en":
    return en_sentence
  else:
    print("Please provide a valid language code.")

