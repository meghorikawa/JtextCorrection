# JtextCorrection
A fine-tuned model on L2 Japanese to provide corrections for texts. A final project for Transformer-Based Language Models course.

# Absract

In this project the state of the art transformer architecture was applied to the domain of learning Japanese as a second language. Much research in the area of computer assisted language learning (CALL) has predominantly focused on English, there is a scarcity of tools available to support learners of other languages. The TEC-JL, Japanese learner error corpus was used to fine-tune an encoder-decoder transformer model, mT5 small and base variants on the downstream task of grammatical error correction (GEC).

Neither model surpassed the GLEU scores achieved by a a CNN architecture model from Koyama et. al 2021 . Nevertheless, the findings illustrate insights and opportunities for possible future investigation - highlighting some of the inherent complexities of processing learner language.

# Summary of files

* **data** contains the model generated predictions, as well as the fine-tuning log from the training.
* **notebooks** contains copies of the notebooks used on google colab to execute the fine-tuning for both small and base models

# Citations

Mizumoto Tomoya, Mamoru Komachi, Masaaki Nagata, and Yuji Matsumoto. Mining
Revision Log of Language Learning SNS for Automated Japanese Error Correction
of Second Language Learners.  In Proceedings of the 5th International Joint
Conference on Natural Language Processing, pp.147-155. Chiang Mai, Thailand,
November 2011.
