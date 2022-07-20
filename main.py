import documentsCollection
import queury

def getSimilarity(DocumentsDirPath, userQueury):
    collection = documentsCollection.DocumentsCollection("Coleção de Documentos dos Slides", 4,
                                     DocumentsDirPath)
    collection.setDocCollectionVocabulary()
    collection.setDocumentsTF_IDF()
    collection.setDocumentsNormalization()

    q = queury.Queury(userQueury)
    q.getQueuryTF_IDF(collection)
    q.setNormalization()

    for doc in collection.documents_list:
        numerator = 0.0
        denominator = doc.documentNormalization * q.normalization
        for term, tf_idf in q.TF_IDF_Dict.items():
            termTFIDF = doc.dictTF_IDF.get(term)
            if termTFIDF != None:
                numerator = numerator + (tf_idf * doc.dictTF_IDF.get(term))
        sim = numerator / denominator
        collection.dictDocQueurySimilarity.update({doc.name: sim})
        
    showRankedDocuments(collection, q)

def showRankedDocuments(collection, queury):
    print(collection.name)
    print('')
    print("Consulta do usuário: " + queury.content)
    print('')
    print("Ranqueamento dos Documentos:")
    print("Nome do documento    Similaridade")
    simDict = collection.dictDocQueurySimilarity
    for documentName in sorted(simDict, key = simDict.get, reverse = True):
        print(documentName, "               ", round(simDict[documentName], 4))

### main ###
getSimilarity("/home/gusta/python/ModeloVetorial/documents", "or not to")
