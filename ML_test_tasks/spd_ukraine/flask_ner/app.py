from flask import Flask,render_template,request
import pandas as pd
import spacy
nlp_en = spacy.load('en_core_web_sm')
nlp_uk = spacy.load('uk_core_news_sm')


app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/get-entities', methods=["GET"]) #GET
def get_entities():
	if request.method == 'GET':
		args = request.args
		choice = args.get('taskoption')
		rawtext = args.get('rawtext')
		if len(rawtext)==0 | len(rawtext)>300:
			return 'Text is too long or too short!'

		if  choice == 'en':
			doc = nlp_en(rawtext)
			d = []
			results = {}
			num_of_results = 0
			for ent in doc.ents:
				d.append((ent.label_, ent.text))
				df = pd.DataFrame(d, columns=('named entity', 'output'))
				per = df.loc[df['named entity']=='PERSON']['output']
				loc = df.loc[df['named entity']=='GPE']['output']
				results["persons"] = per.tolist()
				results["locations"] = loc.tolist()
				num_of_results = len(per)+ len(loc)

		elif choice == 'uk':
			doc = nlp_uk(rawtext)
			d = []
			results = {}
			num_of_results = 0
			for ent in doc.ents:
				d.append((ent.label_, ent.text))
				df = pd.DataFrame(d, columns=('named entity', 'output'))
				per = df.loc[df['named entity']=='PER']['output']
				loc = df.loc[df['named entity']=='LOC']['output']
				results["persons"] = per.tolist()
				results["locations"] = loc.tolist()
				num_of_results = len(per) + len(loc)
		else:
			return 'Choose the language next time!'

	
	return render_template("index.html",results=results,num_of_results = num_of_results)


if __name__ == '__main__':
	app.run(port=8888, debug=True)