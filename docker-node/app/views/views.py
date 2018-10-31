from app import app

@app.route('/app', methods=['GET', 'POST'])
def start():    
    if request.method == 'POST':
        start_angle = request.values.get("start_angle")
        end_angle  = request.values.get("end_angle")
        n_angles = request.values.get("n_angles")


        return render_template("hold.html", start_angle = start_angle, end_angle = end_angle,
				 n_angles = n_angles )

    return render_template("home.html")
