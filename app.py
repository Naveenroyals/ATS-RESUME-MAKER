from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html')
@app.route('/create_resume')
def create_resume():
    return render_template('create_resume.html')
@app.route('/edit_resume')
def edit_resume():
    return render_template('edit_resume.html')
@app.route('/update_resume')
def update_resume():
    return render_template('update_resume.html')
@app.route('/delete_resume')
def delete_resume():
    return render_template('delete_resume.html')
@app.route('/view_resumes')
def view_resumes():
    return render_template('view_resumes.html')
@app.route('/settings')
def settings():
    return render_template('settings.html')
@app.route('/help')
def help_page():
    return render_template('help.html')
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')
@app.route('/resources')
def resources():
    return render_template('resources.html')
@app.route('/legal_notice')
def legal_notice():
    return render_template('legal_notice.html')
@app.route('/terms_of_service')
def terms_of_service():
    return render_template('terms_of_service.html')
@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')
@app.route('/faq')
def faq():
    return render_template('faq.html')
if __name__ == '__main__':
    app.run(debug=True)
