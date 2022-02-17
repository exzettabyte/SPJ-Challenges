from flask import Flask, render_template_string,render_template, request, url_for

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		nama = request.form['nama']
		email = request.form['email']
		template = '''
<!DOCTYPE html>
	<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>Wedding</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link href="https://fonts.googleapis.com/css?family=Montez" rel="stylesheet">
	<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,700,300' rel='stylesheet' type='text/css'>
	<link rel="stylesheet" href="{{ url_for('static', filename='css/animate.css') }}">
	<link rel="stylesheet" href="{{ url_for('static', filename='css/icomoon.css') }}">
	<link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.css') }}">
	<link rel="stylesheet" href="{{ url_for('static', filename='css/superfish.css') }}">
	<link rel="stylesheet" href="{{ url_for('static', filename='css/magnific-popup.css') }}">
	<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }} ">
	<script src="{{ url_for('static', filename='js/modernizr-2.6.2.min.js') }}"></script>
	<script src="{{ url_for('static', filename='dist/scripts.min.js') }}"></script>
	</head>
	<body>
		<div id="fh5co-wrapper">
		<div id="fh5co-page">
		<div class="fh5co-hero" data-section="home">
			<div class="fh5co-overlay"></div>
			<div class="fh5co-cover text-center" data-stellar-background-ratio="0.5" style="background-image: url(../static/images/cover_bg_1.jpg);">
				<div class="display-t">
					<div class="display-tc">
						<div class="container">
							<div class="col-md-10 col-md-offset-1">
								<div class="animate-box">
									<h1>The Wedding</h1>
									<h2>Thomas &amp; Audrey</h2>
									<p><span>28.12.2044</span></p>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<header id="fh5co-header-section" class="sticky-banner">
			<div class="container">
				<div class="nav-header">
					<a href="#" class="js-fh5co-nav-toggle fh5co-nav-toggle dark"><i></i></a>
					<h1 id="fh5co-logo"><a href="{{ url_for('index') }}">Nuptial</a></h1>
					<!-- START #fh5co-menu-wrap -->
					<nav id="fh5co-menu-wrap" role="navigation">
						<ul class="sf-menu" id="fh5co-primary-menu">
							<li class="active"><a href="{{ url_for('index') }}" >Home</a></li>
							<li><a href="{{ url_for('location') }}">When &amp; Where</a></li>
							<li><a href="{{ url_for('donation') }}">Donation</a></li>
						</ul>
					</nav>
				</div>
			</div>
		</header>
		
		<div id="fh5co-couple" class="fh5co-section-gray">
			<div class="container">
				<div class="row row-bottom-padded-md animate-box">
					<div class="col-md-6 col-md-offset-3 text-center">
						<div class="col-md-5 col-sm-5 col-xs-5 nopadding">
							<img src="{{ url_for('static', filename='images/shelby.jpg') }}" class="img-responsive">
							<h3>Thomas Shelby</h3>
						</div>
						<div class="col-md-2 col-sm-2 col-xs-2 nopadding"><h2 class="amp-center"><i class="icon-heart"></i></h2></div>
						<div class="col-md-5 col-sm-5 col-xs-5 nopadding">
							<img src="{{ url_for('static', filename='images/123.jpg') }}" class="img-responsive">
							<h3>Audrey Nathania</h3>
						</div>
					</div>
				</div>
				<div class="row animate-box">
					<div class="col-md-8 col-md-offset-2">
						<div class="col-md-12 text-center heading-section">
							<h2>Are Getting Married</h2>
							<p><strong>on Dec 28, 2044 &mdash; Odescalchi Castle, Italy</strong></p>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div id="fh5co-countdown">
			<div class="row">
				<div class="col-md-8 col-md-offset-2 text-center animate-box">
					<p class="countdown">
						<span id="days"></span>
						<span id="hours"></span>
						<span id="minutes"></span>
						<span id="seconds"></span>
					</p>
				</div>
			</div>
		</div>

		<div id="fh5co-started" style="background-image:url(../static/images/cover_bg_2.jpg);" data-stellar-background-ratio="0.5">
		<div class="overlay"></div>
			<div class="container">
				<div class="row animate-box">
					<div class="col-md-8 col-md-offset-2 text-center heading-section">
						<h2>Are You Attending?</h2>
						<p>Thank you %s for attending</p>
					</div>
				</div>
			</div>
		</div>
		<footer>
			<div id="footer">
				<div class="container" >
					<div class="row">
						<div class="col-md-12 text-center">
							<h2>Thomas &amp; Audrey</h2>
						</div>
						<div class="col-md-6 col-md-offset-3 text-center">
							<p class="fh5co-social-icons">
								<a href="#"><i class="icon-twitter2"></i></a>
								<a href="#"><i class="icon-facebook2"></i></a>
								<a href="#"><i class="icon-youtube"></i></a>
							</p>
							<p>2021</p>
						</div>
					</div>
				</div>
			</div>
		</footer>
	</div>
	</div>
	</body>
</html>
''' % nama
		return render_template_string(template)
	return render_template('index.html')

@app.route('/location',methods=['GET'])
def location():
	return render_template('location.html')

@app.route('/donation',methods=['GET'])
def donation():
	return render_template('donation.html')

if __name__ == '__main__':
	app.run(debug=False,host='0.0.0.0')
