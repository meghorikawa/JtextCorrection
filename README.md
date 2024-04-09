# JtextCorrection
A fine-tuned model on L2 Japanese to provide corrections for texts. A final project for Transformer-Based Language Models course.

# Absract

In this project the state of the art transformer architecture was applied to the domain of learning Japanese as a second language. Much research in the area of computer assisted language learning (CALL) has predominantly focused on English, there is a scarcity of tools available to support learners of other languages. The TEC-JL, Japanese learner error corpus was used to fine-tune an encoder-decoder transformer model, mT5 small and base variants on the downstream task of grammatical error correction (GEC).

Neither model surpassed the GLEU scores achieved by a a CNN architecture model from Koyama et. al 2021 . Nevertheless, the findings illustrate insights and opportunities for possible future investigation - highlighting some of the inherent complexities of processing learner language.

# Summary of files

* **data** contains the model generated predictions, as well as the fine-tuning log from the fine-tuning.
* **notebooks** contains copies of the notebooks used on google colab to execute the fine-tuning for both small and base models

# Citations

Christopher Bryant and Ted Briscoe. 2018. Language
model based grammatical error correction without
annotated training data. In Proceedings of the Thirteenth
Workshop on Innovative Use of NLP for Building
Educational Applications, pages 247–253, New
Orleans, Louisiana. Association for Computational
Linguistics.

Shamil Chollampatt and Hwee Tou Ng. 2017. Connecting
the dots: Towards human-level grammatical error
correction. In Proceedings of the 12th Workshop on
Innovative Use of NLP for Building Educational Applications,
pages 327–333, Copenhagen, Denmark.
Association for Computational Linguistics.

Aomi Koyama, Tomoshige Kiyuna, Kenji Kobayashi,
Mio Arai, and Mamoru Komachi. 2020. Construction
of an evaluation corpus for grammatical error
correction for learners of Japanese as a second language.
In Proceedings of the Twelfth Language Resources
and Evaluation Conference, pages 204–211,
Marseille, France. European Language Resources
Association.

Detmar Meurers. 2015. Learner corpora and natural
language processing, Cambridge Handbooks in Language
and Linguistics, page 537–566. Cambridge
University Press.

Tomoya Mizumoto, Mamoru Komachi, Masaaki Nagata,
and Yuji Matsumoto. 2011. Mining revision log of
language learning SNS for automated Japanese error
correction of second language learners. In Proceedings
of 5th International Joint Conference on Natural
Language Processing, pages 147–155, Chiang Mai,
Thailand. Asian Federation of Natural Language Processing.

Courtney Napoles, Keisuke Sakaguchi, Matt Post, and
Joel Tetreault. 2015. Ground truth for grammatical
error correction metrics. In Proceedings of the 53rd
Annual Meeting of the Association for Computational
Linguistics and the 7th International Joint Conference
on Natural Language Processing (Volume 2:
Short Papers), pages 588–593, Beijing, China. Association
for Computational Linguistics.

Courtney Napoles, Keisuke Sakaguchi, Matt Post, and
Joel Tetreault. 2016. GLEU without tuning. eprint
arXiv:1605.02592 [cs.CL].

Hwee Tou Ng, Siew Mei Wu, Ted Briscoe, Christian
Hadiwinoto, Raymond Hendy Susanto, and Christopher
Bryant. 2014. The CoNLL-2014 shared task
on grammatical error correction. In Proceedings of
the Eighteenth Conference on Computational Natural
Language Learning: Shared Task, pages 1–14,
Baltimore, Maryland. Association for Computational
Linguistics.

Keisuke Sakaguchi, Matt Post, and Benjamin
Van Durme. 2017. Grammatical error correction
with neural reinforcement learning. In Proceedings
of the Eighth International Joint Conference on Natural
Language Processing (Volume 2: Short Papers),
pages 366–372, Taipei, Taiwan. Asian Federation of
Natural Language Processing.

Milan Straka, Jakub N´aplava, and Jana Strakov´a. 2021.
Character transformations for non-autoregressive
GEC tagging. In Proceedings of the Seventh Workshop
on Noisy User-generated Text (W-NUT 2021),
pages 417–422, Online. Association for Computational
Linguistics.

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz
Kaiser, and Illia Polosukhin. 2023. Attention is all
you need.

Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel,
Barret Zoph, Sebastian Borgeaud, Dani Yogatama,
Maarten Bosma, Denny Zhou, Donald Metzler, Ed H.
Chi, Tatsunori Hashimoto, Oriol Vinyals, Percy
Liang, Jeff Dean, and William Fedus. 2022. Emergent
abilities of large language models.

Linting Xue, Noah Constant, Adam Roberts, Mihir Kale,
Rami Al-Rfou, Aditya Siddhant, Aditya Barua, and
Colin Raffel. 2021. mt5: A massively multilingual
pre-trained text-to-text transformer.

Michihiro Yasunaga, Jure Leskovec, and Percy Liang.
2021. LM-critic: Language models for unsupervised
grammatical error correction. In Proceedings of the
2021 Conference on Empirical Methods in Natural
Language Processing, pages 7752–7763, Online and
Punta Cana, Dominican Republic. Association for
Computational Linguistics.

Zheng Yuan and Ted Briscoe. 2016. Grammatical error
correction using neural machine translation. In
Proceedings of the 2016 Conference of the North
American Chapter of the Association for Computational
Linguistics: Human Language Technologies,
pages 380–386, San Diego, California.
