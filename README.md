# PhonemeReplacer
A script for replacing the phoneme in the lab and/or ust.

This script is mainly written for NNSVS/ENUNU label batch replace for the convenience of not having to edit each and individual file manually.

This script was written due to the discussion of "having no br (breath) label and label them as pau will be more beneficial to the model", and it has been proven to be true after some testing in a lot of different models and languages.

So basically what these script will do is it will change ALL of the lab/ust files format in the folder that the script is in to .txt format, and do an action of "control-f. replace all" with whatever in the config (it will change br to pau for PhonemeReplacer4Lab, and br to R for PhonemeReplacer4Ust by default). Then it will automatically change the extension from .txt back to it's original extension.

# How to use and Edit the Config

- Using
1. Put the script in the folder containing the files that you want to batch replace. (be sure to use the correct script for each file type)
3. Run the script

- Editing Config

Edit the old_phoneme with whatever you want to replace and new_phoneme with whatever you want to replace it with (PhonemeReplacer4Lab)
Edit the old_lyric with whatever you want to replace and new_lyric with whatever you want to replace it with (PhonemeReplacer4Ust)
