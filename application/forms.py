from wtforms import (
	Form,
	StringField,
	SelectMultipleField,
	RadioField,
	DateField,
	TimeField,
	IntegerField,
	SelectField,
	SubmitField
)
from wtforms.validators import (
	NumberRange,
	InputRequired,
	ValidationError
)
from flask_wtf import FlaskForm
import requests
from datetime import datetime


########## START Data Transfer Forms ##########

"""Form for Smart Meter (Windows) Page"""
class DataTransfer_Form(Form):

	#### Transfer Type: Both Now & Schedule ####
	data_source = StringField(
		label="Data Source",
		validators=[
			InputRequired()],
		render_kw={"disabled": ""})

	meters = SelectMultipleField(
		label="Meters",
		validators=[
			InputRequired()])

	transfer_type = RadioField(
		label="Transfer Type",
		choices=["Now", "Schedule"],
		default="Now",
		validators=[
			InputRequired()],
		render_kw={"onclick": "toggle_transfer_type(this.id)"})

	start_time = TimeField(
		label="Data Start Time",
		format="%H:%M:%S",
		default=datetime(2023, 1, 1, hour=12),
		validators=[
			InputRequired()],
		render_kw={"step": "1", })


	#### Wireshark Data: WiresharkData only ####
	wireshark_source = RadioField(
		label="Wireshark Source",
		choices=["Ethernet", "WiFi"],
		default="Ethernet")


	#### Transfer Type: Now only ####
	date = DateField(
		label="Date",
		validators=[
			InputRequired()],
		default=datetime(2023, 1, 1))

	end_time = TimeField(
		label="Data End Time",
		format="%H:%M:%S",
		default=datetime(2023, 1, 1, hour=12),
		validators=[
			InputRequired()],
		render_kw={"step": "1"})


	#### Transfer Type: Schedule only ####
	transfer_freq = RadioField(
		label="Transfer Frequency",
		choices=["Daily", "Weekly", "Monthly"],
		render_kw={"onclick": "toggle_transfer_freq(this.id)"})

	transfer_freq_time = TimeField(
		label="At",
		format="%H:%M",
		default=datetime(2023, 1, 1, hour=12),
		validators=[
			InputRequired()])

	transfer_freq_week = SelectMultipleField(
		label="on a",
		validators=[
			InputRequired()])
	transfer_freq_week_time = TimeField(
		label="At",
		format="%H:%M",
		default=datetime(2023, 1, 1, hour=12),
		validators=[
			InputRequired()])

	transfer_freq_month = IntegerField(
		label="on the",
		default=1,
		validators=[
			InputRequired(),
			NumberRange(min=1, max=31, message="Invalid day of month")],
		render_kw={"style": "width:50px; margin: 0px 5px 0px 0px"})
	transfer_freq_month_time = TimeField(
		label="At",
		format="%H:%M",
		default=datetime(2023, 1, 1, hour=12),
		validators=[
			InputRequired()])

	transfer_dur = SelectField(
		label="Data to Download",
		choices=[1, 5, 10, 15, 30],
		default=5,
		validators=[
			InputRequired()],
		render_kw={"style": "width:45px; margin: 0px 5px 0px 0px"})

	job_name = StringField(
		label="Job Name",
		default="New Job",
		validators=[
			InputRequired()],
		render_kw={"placeholder": "Enter a job name"})

	submit = SubmitField("Data Transfer", render_kw={"id": "div_btn"})


########## END Data Transfer Forms ##########
########## START Spider Forms ##########

"""Form for Spider Submit Job Page"""
def url_check(form, field):
	try:
		if requests.get(field.data).status_code != 200:
			raise
	except:
		raise ValidationError("A valid HTTP/S link must be provided: {}".format(field.data))
	if "github.com" not in field.data:
		raise ValidationError("A GitHub repository link must be provided")

class Spider_Form(FlaskForm):

	githubUrl = StringField(
		label="Input URL:",
		validators=[
			InputRequired(),
			url_check])

	scrapingDepth = SelectField(
		"Scraping Depth: ",
		choices=[("0", "0"), ("1", "1"), ("2", "2")])

	spiderChoice = SelectField(
		"Spider: ",
		choices=[("github", "github")])

	submit = SubmitField(
		label="Submit URL")


########## END Spider Forms ##########
########## START Admin Forms ##########

"""Form for Admin Data Transfer Page"""
class AdminConfig_DataTransfer_Form(Form):

	windows_ip = StringField(
		"Windows IP",
		validators=[
			InputRequired()])

	debian_ip = StringField(
		"Debian IP",
		validators=[
			InputRequired()])

	ftp_user = StringField(
		"FTP User",
		validators=[
			InputRequired()])

	ftp_pw = StringField(
		"FTP Password",
		validators=[
			InputRequired()])

	cron_user = StringField(
		"Host Username",
		validators=[
			InputRequired()])


"""Form for Admin App Launch Page"""
class AdminConfig_AppLaunch_Form(Form):
	arkime_user = StringField(
		"Arkime Username",
		validators=[
			InputRequired()])

	arkime_password = StringField(
		"Arkime Password",
		validators=[
			InputRequired()])


"""Form for Admin Network Capture Page"""
class AdminConfig_NetworkCapture_Form(Form):
	capture_path = StringField(
		"PCAP File Path",
		validators=[
			InputRequired()])


########## END Admin Forms ##########
