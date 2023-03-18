from flask import Flask, request
app = Flask(__name__)

@app.route('/') # Nova rota
def main():
    primeira = request.args.get('primeira')
    segunda = request.args.get('segunda')


    if primeira and segunda:
        primeira = float(primeira)
        segunda = float(segunda)
        media = (primeira+segunda)/2

        if media >= 7:
            resultado = 'Aprovado'
        elif media >= 4:
            resultado = 'Recuperação'
        else:
            resultado = 'Reprovado'

        resultado += f' (média {media:.1f})'

    return resultado

             
        
if __name__ == '__main__' :
    app.run(debug=True)
