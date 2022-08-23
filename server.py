from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
#Root that allows for increments by one when entered.
def initialize_root():
    if 'site_visit_count' not in session:
        session['site_visit_count'] = 0
    else:
        session['site_visit_count'] += 1
    print("Session",session)
    return render_template('index.html')


@app.route('/reset')
#Removes all values from the session.
def reset():
    session.clear()
    return redirect('/')

@app.route('/add_two')
#Allows for additional increment to be added. Forming a double.
def double():
    session['site_visit_count'] += 1
    return redirect('/')

@app.route('/input', methods=['POST'])
#Allows the user to enter a specific increment via a form.
def user_input_counter():
    session['site_visit_count'] += int(request.form['input_increment']) - 1
    print(request.form)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)