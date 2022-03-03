from flask import *
from weatherfunction import *
app = Flask(__name__,template_folder="templates",static_url_path="/static")

@app.route("/")
def uttarkand():
   return  render_template('uttarakhand.html')

@app.route("/DEHRADUN")
def getweather_dehradun():
    a= weather_info("DEHRADUN")
    return  render_template('dehradun.html',d_t=a[0], fahrenheit=a[1],celsius=a[2], condition=a[3], icon="https:"+str(a[4]))

@app.route("/ALMORA")
def getweather_almora():
    a = weather_info("almora")

    return  render_template('almora.html',d_t=a[0], fahrenheit=a[1],celsius=a[2], condition=a[3], icon="https:"+str(a[4]))

@app.route("/BAGESHWAR")
def getweather_bageshwar():
    a = weather_info("bageshwar")
    return  render_template('bageshwar.html',d_t=a[0], fahrenheit=a[1],celsius=a[2], condition=a[3], icon="https:"+str(a[4]))

@app.route("/CHAMPAWAT")
def getweather_champawat():
    a = weather_info("champawat")
    return  render_template('champawat.html',d_t=a[0], fahrenheit=a[1],celsius=a[2], condition=a[3], icon="https:"+str(a[4]))

@app.route("/CHAMOLI")
def getweather_chamoli():
    a = weather_info("chamoli")
    return  render_template('chamoli.html',d_t=a[0], fahrenheit=a[1],celsius=a[2], condition=a[3], icon="https:"+str(a[4]))

@app.route("/NAINITAL")
def getweather_nainital():
    a = weather_info("Kumaon")
    return  render_template('nainital.html',d_t=a[0], fahrenheit=a[1],celsius=a[2], condition=a[3], icon="https:"+str(a[4]))

@app.route("/PAURI_GARHWAL")
def getweather_pauri_garhwal():
    a = weather_info("pauri")
    return  render_template('Pauri_garhwal.html',d_t=a[0], fahrenheit=a[1],celsius=a[2], condition=a[3], icon="https:"+str(a[4]))

@app.route("/PITHORAGARH")
def getweather_Pithoragarh():
    a = weather_info("Pithoragarh")
    return  render_template('Pithoragarh.html',d_t=a[0], fahrenheit=a[1],celsius=a[2], condition=a[3], icon="https:"+str(a[4]))

@app.route("/HARIDWAR")
def getweather_haridwar():
    a = weather_info("haridwar")
    return  render_template('Haridwar.html',d_t=a[0], fahrenheit=a[1],celsius=a[2], condition=a[3], icon="https:"+str(a[4]))

@app.route("/SINGH_NAGAR")
def getweather_singh_nagar():
    a = weather_info("singh nagar")
    return  render_template('singh_nagar.html',d_t=a[0], fahrenheit=a[1],celsius=a[2], condition=a[3], icon="https:"+str(a[4]))


@app.route("/UTTARKASHI")
def getweather_utkarshi():
    a = weather_info("uttarkashi")
    return  render_template('uttarkashi.html',d_t=a[0], fahrenheit=a[1],celsius=a[2], condition=a[3], icon="https:"+str(a[4]))

@app.route("/RUDRAPRAYAG")
def getweather_rudraprayag():
    a = weather_info("rudraprayag")


    return  render_template('Rudraprayag.html',d_t=a[0], fahrenheit=a[1],celsius=a[2], condition=a[3], icon="https:"+str(a[4]))
@app.route("/TEHRI_GARHWAL")
def getweather_Tehri_garhwal():
    a = weather_info("Tehri garhwal")
    return  render_template('Tehri_garhwal.html',d_t=a[0], fahrenheit=a[1],celsius=a[2], condition=a[3], icon="https:"+str(a[4]))


@app.route("/error")
def error():
    return render_template("error.html")




if __name__ == '__main__':
    app.run(debug=True)
