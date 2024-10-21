# Dr.Chats

#### DISCLAIMER - This is a Beta test bot and not intended for Medical Diagnosis. Should you have any medical concerns, please contact your medical provider. 
#### Q&A_Med_chat.ipynb is the main dataset 

## Overview
Dr. Chats is an AI-driven chatbot that focuses on medical data analysis, specifically leveraging public datasets such as PubMed to provide insightful responses. It integrates AI techniques to help in healthcare, offering potential support for clinicians and researchers.

## Features
- Chatbot capabilities using healthcare data (e.g., PubMed, Huggingface - AI Medical General Dataset).
- Analysis of medical datasets including STI-related data and scientific literature.
- Integration with pre-trained AI models to enhance conversational experience.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sug-ar-N-Spice/Dr.Chats.git
   ```
2. Navigate to the project directory:
```bash
cd Dr.Chats
```
## Install dependencies: 
Follow the package requirements in the Jupyter Notebooks (e.g., via pip or conda).

### Model Implementation
```python
! pip install sacremoses
! pip install transformers
! pip install datasets
! pip install torch
```

#### Libraries 
1. Hugging Face
2. Sentence Transformers
3. AI Medical

### Model Implementation


## Usage
The project contains multiple Jupyter notebooks like Dr_chat_pre.ipynb and Pub_med_dr_chat.ipynb that allow you to run AI models on medical data.

Datasets such as `pmc_dataset.csv` are included for analysis. Full datasets can be found on the following Google Drive links:

* [ai_medical_dataset.zip](https://drive.google.com/file/d/1OK2njdhp7QMvFvydN_jm0K4Posv9yX_t/view?usp=sharing) - Contains a tab separated file with all of the medical data.

You can customize and extend the chatbot to work with additional datasets or models.

## Contributing
We welcome contributions to improve the features and capabilities of Dr. Chats. Please submit a pull request or open an issue if you encounter bugs or have suggestions.


## Contact
For questions or collaborations, please contact the maintainers via GitHub.

* Ty - https://github.com/tyzwhitt
* Jerome- https://github.com/exohuman 
* Simon- https://github.com/Simonpnce57
* Idowu- https://github.com/jubjam18
* Patricia - https://github.com/Sug-ar-N-Spice
  
## License & References 

1. The AI Medical General Dataset is licensed under the CC-BY 4.0 license

* @dataset{ai_medical_dataset,
  title = {AI Medical Dataset},
  author = {Ruslan Magana Vsevolodovna},
  year = {2023},
  url = {https://github.com/ruslanmv/ai-medical-chatbot},
}

2. @article{10.1093/bib/bbac409,
    author = {Luo, Renqian and Sun, Liai and Xia, Yingce and Qin, Tao and Zhang, Sheng and Poon, Hoifung and Liu, Tie-Yan},
    title = "{BioGPT: generative pre-trained transformer for biomedical text generation and mining}",
    journal = {Briefings in Bioinformatics},
    volume = {23},
    number = {6},
    year = {2022},
    month = {09},
    abstract = "{Pre-trained language models have attracted increasing attention in the biomedical domain, inspired by their great success in the general natural language domain. Among the two main branches of pre-trained language models in the general language domain, i.e. BERT (and its variants) and GPT (and its variants), the first one has been extensively studied in the biomedical domain, such as BioBERT and PubMedBERT. While they have achieved great success on a variety of discriminative downstream biomedical tasks, the lack of generation ability constrains their application scope. In this paper, we propose BioGPT, a domain-specific generative Transformer language model pre-trained on large-scale biomedical literature. We evaluate BioGPT on six biomedical natural language processing tasks and demonstrate that our model outperforms previous models on most tasks. Especially, we get 44.98\%, 38.42\% and 40.76\% F1 score on BC5CDR, KD-DTI and DDI end-to-end relation extraction tasks, respectively, and 78.2\% accuracy on PubMedQA, creating a new record. Our case study on text generation further demonstrates the advantage of BioGPT on biomedical literature to generate fluent descriptions for biomedical terms.}",
    issn = {1477-4054},
    doi = {10.1093/bib/bbac409},
    url = {https://doi.org/10.1093/bib/bbac409},
    note = {bbac409},
    eprint = {https://academic.oup.com/bib/article-pdf/23/6/bbac409/47144271/bbac409.pdf},
}

3. PyMed Code (did not work)

@dataset{Pubmed,
  title = {PyMed-PubMed Access through Python},
  author = {Gijs Wobben},
  year = {2019},
  url = {https://pypi.org/project/pymed/},



