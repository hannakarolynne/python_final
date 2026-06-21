from flask import *
from dotenv import load_dotenv
import os
from supabase import create_client

load_dotenv()
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')

supabase = create_client(supabase_url, supabase_key)

app = Flask(__name__)
app.secret_key= os.getenv('PASSWORD')

@app.route("/")
# @app.route("/login", methods=['GET', 'POST'])
# def index():
#     texto = "teste"
#     if request.method == "GET":
#         email = request.form.get('email')
#         senha = request.form.get('senha')
#         print(email, senha)
#         resposta = supabase.table("usuarios").select("*").eq("email",email).eq("senha", senha).execute()
#         if len(resposta.data) > 0:
#             print(resposta)
#             session[id] = resposta.data[0]['id']
#             texto
#         else:
#             print('Usuário não registrado')
#         return render_template('login.html')


# REGISTRO
@app.route("/register", methods=['GET','POST'])
def register():
    return render_template('register.html')
    if request.method == "POST" and 'password' in request.form and 'email' in request.form:
        email = request.form('email')
        senha = request.form('senha')
        # print(email, senha)
        inserir = supabase.table("usuarios").insert({"email": email, "senha": senha}).execute()
        if len(inserir.data) > 0:
            session[id] = inserir.data[0]['id']
            return render_template('acessoCliente.html')
        else:
            print('erro')
            return render_template('register.html')
        

if __name__ == '__main__':
    app.run(debug=True)
       