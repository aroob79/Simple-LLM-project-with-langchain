# from langchain_community.llms import GooglePalm
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from keys import api_keys

llm = GoogleGenerativeAI(model="models/text-bison-001",
                         google_api_key=api_keys, temperature=0.5)
# llm = GooglePalm(google_api_key=api_keys, temperature=0.7)


def name_and_items(name):
    prompt1 = PromptTemplate(input_variables=['country_name'],
                             template="suggest a new restaurent name of the following country {country_name}. please give one name.")
    prompt2 = PromptTemplate(input_variables=['restaurent_name'],
                             template="please suggest food menu of the following restaurent {restaurent_name}")
    chain1 = LLMChain(llm=llm, prompt=prompt1, output_key='restaurent_name')
    chain2 = LLMChain(llm=llm, prompt=prompt2, output_key='food_items')
    sequential_chain = SequentialChain(chains=[chain1, chain2],
                                       input_variables=['country_name'],
                                       output_variables=['restaurent_name', 'food_items'])
    input_ = {'country_name': name}

    response_ = sequential_chain(input_)

    return response_


if __name__ == '__main__':
    res = name_and_items('pakistan')
    name = res['restaurent_name']
    res_name = res['food_items']
    print(name)
    print(res)
    print(res_name.strip().split('\n'))
