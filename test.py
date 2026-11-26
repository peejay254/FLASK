from  flask  import  *

# initialize the application
app   =  Flask(__name__)

# define your  route/endpoint 
@app.route("/api/home")
# define your  function 
def home() :
    return  "welcome  home"

# define your route/endpoint
@app.route("/api/services")
# define your function 
def  services():
    return  "welcome to our services"













# run  the application
app.run(debug=True)