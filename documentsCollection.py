import os
import math
import document

class DocumentsCollection:
    name = None
    length = None
    documents_list = []
    vocabulary = []
    dictTermsIDF = {}
    dictDocQueurySimilarity = {} #doc.name, sim

    def __init__(self, name, dir_path):
        os.chdir(dir_path)
        self.name = name

        collection_length= 0

        for file in os.listdir():
            collection_length += 1
            file_name = file
            f = open(file, 'rt')
            content = f.read()
            doc = document.Document(file_name, content)
            self.documents_list.append(doc)
        self.length = collection_length


    def set_collection_vocabulary(self):
        for doc in self.documents_list:
            self.vocabulary = self.vocabulary + doc.vocabularyList
        self.vocabulary = list(dict.fromkeys(self.vocabulary))  #retira duplicatas
        self.vocabulary.sort()  #organiza em ordem alfabetica

    def set_tf_idf(self):
        for doc in self.documents_list:
            doc.setDictTF_IDF(self)

    def set_term_idf(self):
        termNi_dict = self.set_term_ni()
        for term, ni in termNi_dict.items():
            relativeFreq = self.length / ni
            IDF = math.log2(relativeFreq)
            self.dictTermsIDF.update({term: IDF})

    def set_term_ni(self):
        termNi_dict = {}
        for term in self.vocabulary:
            ni = 0
            for doc in self.documents_list:
                if term in doc.vocabularyList:
                    ni = ni + 1
                    termNi_dict.update({term: ni})
        return termNi_dict


    def set_doc_normalization(self):
        for doc in self.documents_list:
            doc.setDocumentNormalization()

    def write_vocabulary(self, dir_path, file_name):
        os.chdir(dir_path)
        file = open(file_name, "w")
        for term in self.vocabulary:
            file.write(term + "\n")
        file.close()