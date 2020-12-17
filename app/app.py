import pymysql
from flask import Flask, request, abort

# connect to database
db = pymysql.connect(host="ensembldb.ensembl.org", port=3306, user="anonymous", passwd="", db="ensembl_website_97")
cursor = db.cursor()


app = Flask(__name__)
@app.route('/entryP', methods=['POST', 'GET', 'PUT', 'PATCH'])
def entry():
   gene = request.args.get('gene')
   if request.method == 'POST':
      abort (400, "405 Method Not Allowed for you")
   elif request.method == 'PUT':
      abort (400, "405 Method Not Allowed for you")
   elif request.method == 'PATCH':
      abort (400, "405 Method Not Allowed for you")
   else:
      var = gene
      if (len(var) > 2):
         cursor.execute("SELECT * FROM `gene_autocomplete` WHERE display_label LIKE '%" + var + "%';")
         dicty = {}
         count = 1
         for x in cursor:
            dictn = {}
            dictn["species"] = x[0]
            dictn["ensembl stable ID"] = x[1]
            dictn["gene_name"] = x[2]
            dictn["location"] = x[3]
            dicty[count] = dictn
            count += 1
         return dicty
      else:
         abort(400, "400 HTTP code")

if __name__ == '__main__':
   app.run(debug = True)