import requests

class NlpEngine:
    '''
        Object in charge of Natuarl Language to SparQl translations
    '''
    QUERIES = {'old' : ('''
                        PREFIX dbr: <http://dbpedia.org/resource/>
                        PREFIX dbp: <http://dbpedia.org/property/>
                        SELECT ?dateOfBirth
                        WHERE {
                            VALUES ?name {
                                dbr:[queryObject]
                            }
                            
                            SERVICE <http://dbpedia.org/sparql> {
                                ?name dbp:birthDate ?dateOfBirth .
                            }
                        }
                        ''', 'dateOfBirth', 'is'),
               'population' : ('''
                    PREFIX dbr: <http://dbpedia.org/resource/>
                    PREFIX dbp: <http://dbpedia.org/property/>
                    SELECT ?size
                    WHERE {
                        VALUES ?name {
                            dbr:[queryObject]
                        }
                        
                        SERVICE <http://dbpedia.org/sparql> {
                            ?name dbp:metroAreaPop ?size .
                        }
                    }
               ''', 'size', 'of')
               }

    def buildSparqlQuery(self, inputQuestion):
        '''
        Creates a SPARQL query out a question in natural language
        :param inputQuestion: a String representing a query
        :return: (str, str): a tuple containing query to be executed
                             and the field to be fetched
        '''
        baseQuery, extractField, previousWord = self._findQuery(inputQuestion)
        queryObject = self._extractObject(inputQuestion, previousWord)

        sparqlQuery = baseQuery.replace('[queryObject]',  queryObject)
        return sparqlQuery, extractField

    def _extractObject(self, inputStr, previousWrd):
        '''
            Extract object of the query
        :param inputStr: string representing a question
        :param previousWrd: word just before the object
        :return: string representing object of the queyr
        '''
        words = inputStr.split()
        return '_'.join(words[words.index(previousWrd)+1:])

    def _findQuery(self, inputStr):
        '''
        Find a query given an input STring
        :param inputStr:
        :return: (str, str, str):  a tuple consisting of query, result field and
                                   word to determine boundaries of the object of
                                   the query
        '''
        wordBags = inputStr.split()
        for w in wordBags:
            if w in self.QUERIES.keys():
                return self.QUERIES[w]
        raise Exception('INvalid query')


class Guru:
    def __init__(self, endpoint: str = 'https://query.wikidata.org/sparql'):
        self.endpoint = endpoint
        self.nlpEngine = NlpEngine()

    def ask(self, question: str):
        query, field = self.nlpEngine.buildSparqlQuery(question)
        dpediaData = self._runQuery(query)
        return dpediaData['results']['bindings'][0][field]['value']


    def _runQuery(self, query):
        data = requests.get(self.endpoint, params={'format': 'json', 'query': query})
        return data.json()






