from flask import Flask , render_template , request ,redirect, url_for , flash
from flask_mysqldb import MySQL

app= Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dbcontactos'
mysql = MySQL(app)

#settings
app.secret_key ='mysecretkey'


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contactos')
    data = cur.fetchall()
    return render_template('index.html',contactos = data)

@app.route('/agregar_contacto', methods=['POST'])
def contacto():
    if request.method == 'POST':
       NombreC=request.form['NombreC']
       Telefono=request.form['Telefono']
       Email=request.form['Email']
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO contactos(NombreC,Telefono,Email)VALUES(%s,%s,%s)',
       (NombreC,Telefono,Email))
       mysql.connection.commit() 
       flash('Contacto Agregado Correctamente')     
       return redirect(url_for('Index'))     

@app.route('/editar/<id>')
def get_contacto(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contactos WHERE id = %s',(id))
    data = cur.fetchall()
    return render_template('editar_contacto.html',contacto = data[0])

@app.route('/actualizar/<id>', methods = ['POST'])
def actualizar_contacto(id):
 if request.method == 'POST':
    NombreC = request.form['NombreC']
    Telefono = request.form['Telefono']
    Email = request.form['Email'] 
    cur = mysql.connection.cursor()
    cur.execute(""" 
     UPDATE contactos
     SET NombreC =%s,
         Email =%s,
         Telefono =%s
     WHERE id =%s    
    """,(NombreC,Email,Telefono,id)) 
    mysql.connection.commit() 
    flash('Contacto actualizado ')
    return redirect(url_for('Index'))
    
@app.route('/eliminar/<string:id>')
def eliminar(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contactos WHERE id ={0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('Index'))
if __name__ == '__main__':
    app.run(port = 3000, debug = True)