from flask import *
from database import *



admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	return render_template('adminhome.html') 


@admin.route('/adminmanagestaff', methods=['GET', 'POST']) 
def adminmanagestaff(): 
    data = {}

    if 'action' in request.args:
        action = request.args['action'] 
        staffid = request.args['id'] 
    else:
        action = None

    if action == "delete":
        q = "DELETE FROM staff WHERE staff_id='%s'" % staffid 
        delete(q)
        return redirect(url_for('admin.adminmanagestaff'))	

    if action == 'update':
        qa = "SELECT * FROM staff WHERE staff_id='%s'" % staffid
        r2 = select(qa)
        data['upd'] = r2

    if 'update' in request.form:
        fname = request.form['fname'] 
        lname = request.form['lname'] 
        gender = request.form['gender'] 
        age = request.form['age']
        phone = request.form['phone'] 
        email = request.form['email'] 
        designation = request.form['designation'] 
        qd = "UPDATE staff SET firstname='%s', lastname='%s', gender='%s', age='%s', phone='%s', email='%s', designation='%s' where staff_id='%s'" % (fname, lname, gender, age, phone, email, designation,staffid)
        update(qd)
        return redirect(url_for('admin.adminmanagestaff'))

    if 'submit' in request.form: 
        fname = request.form['fname'] 
        lname = request.form['lname'] 
        gender = request.form['gender'] 
        age = request.form['age']
        phone = request.form['phone'] 
        email = request.form['email'] 
        designation = request.form['designation'] 
        usern = request.form['username'] 
        passw = request.form['password']  
        q = "INSERT INTO login VALUES(null, '%s', '%s', 'staff')" % (usern, passw)    
        id = insert(q) 
        q = "INSERT INTO staff VALUES(null, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (id, fname, lname, gender, age, phone, email, designation) 
        insert(q) 

    q = "SELECT * FROM staff" 
    res = select(q)
    data['staff'] = res 		

    return render_template('adminmanagestaff.html', data=data)  		


@admin.route('/adminmanagecountries',methods=['get','post']) 
def adminmanagecountries():
	data={}
	if 'action' in request.args:
		action=request.args['action'] 
		countryid=request.args['id'] 
	else:
		action=None
	if action=="delete":
		q="delete from countries where country_id='%s'" %(countryid)   
		delete(q)
		return redirect(url_for('admin.adminmanagecountries'))

	if action=="update":
		q="select * from countries where country_id='%s'" %(countryid) 
		res=select(q)
		data['updatecountries']=res
	if 'update' in request.form:
		countr=request.form['country']	
		q="update countries set country='%s' where country_id='%s'" %(countr,countryid) 
		update(q)
		return redirect(url_for('admin.adminmanagecountries')) 

	if 'submit' in request.form:
		countr=request.form['country']
		q="insert into countries values(null,'%s')" %(countr)   
		insert(q) 
		return redirect(url_for('admin.adminmanagecountries')) 
	q="select * from countries"	
	res=select(q) 
	data['countries']=res 
	return render_template('adminmanagecountries.html',data=data)   


@admin.route('/adminmanageplace',methods=['get','post']) 	
def adminmanageplace():
	data={} 
	if 'action' in request.args:
		action=request.args['action'] 
		placeid=request.args['id'] 
	else:
		action=None
	if action=="delete":
		q="delete from place where place_id='%s'" %(placeid) 
		delete(q)
		return redirect(url_for('admin.adminmanageplace')) 

	if action=="update":
		q="select * from place where place_id='%s'" %(placeid)  
		res=select(q)
		data['updateplace']=res
		q1="SELECT country_id,country,(country_id='%s') AS sel FROM countries ORDER BY sel DESC,country_id ASC" %(res[0]['country_id'])  
		res1=select(q1)
		data['updatecountries']=res1  
	if 'update' in request.form: 
		countryid=request.form['country_id'] 
		place=request.form['place'] 
		q="update place set country_id='%s',state_place='%s' where place_id='%s'" %(countryid,place,placeid)  
		update(q)
		return redirect(url_for('admin.adminmanageplace'))    	

	if 'add' in request.form: 
		countryid=request.form['country_id'] 
		place=request.form['place']
		q="insert into place values(null,'%s','%s')" %(countryid,place)  
		insert(q) 
		return redirect(url_for('admin.adminmanageplace')) 
	q="select * from place INNER JOIN countries using(country_id)" 	 

	res=select(q)
	data['place']=res  
	q="select * from countries"   
	res=select(q)
	data['country_id']=res   
	return render_template('adminmanageplace.html',data=data)   

@admin.route('/adminmanageairports',methods=['get','post'])	
def adminmanageairports():
	data={}
	if 'action' in request.args:
		action=request.args['action'] 
		airportid=request.args['id'] 
	else:
		action=None
	if action=="delete":
		q="delete from shipports where shipport_id='%s'" %(airportid) 
		delete(q)
		return redirect(url_for('admin.adminmanageairports'))
	if action=="update":
		q="select * from shipports where shipport_id='%s'" %(airportid)  
		res=select(q)
		data['updateairports']=res
		q1="SELECT place_id,country_id,state_place,(place_id='%s') AS sel FROM place ORDER BY sel DESC,place_id ASC" %(res[0]['place_id'])  
		res1=select(q1)
		data['updateplace']=res1



	if 'update' in request.form:
		placeid=request.form['place_id']
		name=request.form['name']	
		district=request.form['district'] 
		state=request.form['state'] 
		q="update shipports set place_id='%s',name='%s',district='%s',state='%s' where shipport_id='%s'" %(placeid,name,district,state,airportid) 
		update(q)
		return redirect(url_for('admin.adminmanageairports'))  


	if 'add' in request.form:
		placeid=request.form['place_id'] 
		name=request.form['name']
		district=request.form['district'] 
		state=request.form['state']
		q="insert into shipports values(null,'%s','%s','%s','%s')" %(placeid,name,district,state)    
		insert(q) 
		return redirect(url_for('admin.adminmanageairports')) 
	q="select * from shipports INNER JOIN place using(place_id)"  	
	res=select(q) 
	data['airports']=res  
	q="select * from place" 
	res=select(q)
	data['place_id']=res
	return render_template('adminmanageairports.html',data=data) 

	

@admin.route('/adminmanagetypeofseat',methods=['get','post']) 
def adminmanagetypeofseat():
	data={}
	if 'action' in request.args:
		action=request.args['action'] 
		typeid=request.args['id'] 
	else:
		action=None
	if action=="delete":
		q="delete from type where type_id='%s'" %(typeid)  

		delete(q)
		return redirect(url_for('admin.adminmanagetypeofseat')) 

	if action=="update":
		q="select * from type where type_id='%s'" %(typeid) 
		res=select(q)
		data['updatetypeofseat']=res 
	if 'update' in request.form:
		type=request.form['type']	
		q="update type set type='%s' where type_id='%s'" %(type,typeid) 
		update(q)
		return redirect(url_for('admin.adminmanagetypeofseat')) 
	if 'add' in request.form:
		type=request.form['type'] 
		q="insert into type values(null,'%s')" %(type)     
		insert(q) 
		return redirect(url_for('admin.adminmanagetypeofseat')) 
	q="select * from type" 	
	res=select(q) 
	data['type']=res 
	return render_template('adminmanagetypeofseat.html',data=data) 




@admin.route('/admin_manage_foods',methods=['get','post']) 
def admin_manage_foods():
	data={}
	if 'action' in request.args:
		action=request.args['action'] 
		typeid=request.args['id'] 
	else:
		action=None
	if action=="delete":
		q="delete from foods where food_id='%s'" %(typeid)  

		delete(q)
		return redirect(url_for('admin.admin_manage_foods')) 

	if action=="update":
		q="select * from foods where food_id='%s'" %(typeid) 
		res=select(q)
		data['updatetypeofseat']=res 
	if 'update' in request.form:
		type=request.form['type']	
		q="update foods set food_name='%s' where food_id='%s'" %(type,typeid) 
		update(q)
		return redirect(url_for('admin.admin_manage_foods')) 
	if 'add' in request.form:
		type=request.form['type'] 
		q="insert into foods values(null,'%s')" %(type)     
		insert(q) 
		return redirect(url_for('admin.admin_manage_foods')) 
	q="select * from foods" 	
	res=select(q) 
	data['type']=res 
	return render_template('admin_manage_foods.html',data=data) 




@admin.route('/admin_manage_bed_rooms',methods=['get','post']) 
def admin_manage_bed_rooms():
	data={}
	if 'action' in request.args:
		action=request.args['action'] 
		typeid=request.args['id'] 
	else:
		action=None
	if action=="delete":
		q="delete from bedrooms where bedroom_id='%s'" %(typeid)  

		delete(q)
		return redirect(url_for('admin.admin_manage_bed_rooms')) 

	if action=="update":
		q="select * from bedrooms where bedroom_id='%s'" %(typeid) 
		res=select(q)
		data['updatetypeofseat']=res 
	if 'update' in request.form:
		room_name=request.form['type']	
		bed_type=request.form['bed_type']	
		details=request.form['details']	
		q="update bedrooms set bedroom_name='%s',bed_type='%s',details='%s' where bedroom_id='%s'" %(room_name,bed_type,details,typeid) 
		update(q)
		return redirect(url_for('admin.admin_manage_bed_rooms')) 
	if 'add' in request.form:
		room_name=request.form['type'] 
		bed_type=request.form['bed_type']	
		details=request.form['details']	
		q="insert into bedrooms values(null,'%s','%s','%s')" %(room_name,bed_type,details)     
		insert(q) 
		return redirect(url_for('admin.admin_manage_bed_rooms')) 
	q="select * from bedrooms" 	
	res=select(q) 
	data['type']=res 
	return render_template('admin_manage_bed_rooms.html',data=data) 


@admin.route('/admin_manage_company',methods=['get','post']) 
def admin_manage_company():
	data={}
	if 'action' in request.args:
		action=request.args['action'] 
		typeid=request.args['id'] 
	else:
		action=None
	if action=="delete":
		q="UPDATE `login` SET `usertype`='pending' WHERE `login_id`='%s'" %(typeid)  

		delete(q)
		return redirect(url_for('admin.admin_manage_company')) 
	if action=="allow":
		q="UPDATE `login` SET `usertype`='company' WHERE `login_id`='%s'" %(typeid)  

		delete(q)
		return redirect(url_for('admin.admin_manage_company')) 

	if action=="update":
		q="select * from company where login_id='%s'" %(typeid) 
		res=select(q)
		data['updatecompany']=res 
	if 'update' in request.form:
		company_name=request.form['company_name']	
		company_place=request.form['company_place']	
		company_phone=request.form['company_phone']	
		company_email=request.form['company_email']	
		company_address=request.form['company_address']	
		q="update company set company_name='%s',company_place='%s',company_phone='%s',company_email='%s',company_address='%s' where login_id='%s'" %(company_name,company_place,company_phone,company_email,company_address,typeid) 
		update(q)
		return redirect(url_for('admin.admin_manage_company')) 
	if 'add' in request.form:
		company_name=request.form['company_name']	
		company_place=request.form['company_place']	
		company_phone=request.form['company_phone']	
		company_email=request.form['company_email']	
		company_address=request.form['company_address']	
		username=request.form['username']	
		password=request.form['password']	
		qin="select * from login where username='%s' or password='%s'"%(username,password)
		ress=select(qin)
		if ress:
			flash("sorry username or password already exists try again")
		else:
			q="insert into login values(null,'%s','%s','company')" %(username,password)     
			res=insert(q) 
			q="insert into company values(null,'%s','%s','%s','%s','%s','%s',curdate())" %(res,company_name,company_place,company_phone,company_email,company_address)     
			insert(q) 
			return redirect(url_for('admin.admin_manage_company')) 
	q="select * from company inner join login using(login_id)" 	
	res=select(q) 
	data['type']=res 
	return render_template('admin_manage_company.html',data=data) 




@admin.route('/admin_manage_mechanic',methods=['get','post']) 
def admin_manage_mechanic():
	data={}
	if 'action' in request.args:
		action=request.args['action'] 
		typeid=request.args['id'] 
	else:
		action=None
	if action=="delete":
		q="UPDATE `login` SET `usertype`='pending' WHERE `login_id`='%s'" %(typeid)  

		delete(q)
		return redirect(url_for('admin.admin_manage_mechanic')) 
	if action=="allow":
		q="UPDATE `login` SET `usertype`='mechanic' WHERE `login_id`='%s'" %(typeid)  

		delete(q)
		return redirect(url_for('admin.admin_manage_mechanic')) 

	if action=="update":
		q="select * from mechanics where login_id='%s'" %(typeid) 
		res=select(q)
		data['updatecompany']=res 
	if 'update' in request.form:
		mech_name=request.form['company_name']	
		mech_place=request.form['company_place']	
		mech_phone=request.form['company_phone']	
		mech_email=request.form['company_email']	
		mech_address=request.form['company_address']	
		q="update mechanics set mech_name='%s',mech_place='%s',mech_phone='%s',mech_email='%s',mech_address='%s' where login_id='%s'" %(mech_name,mech_place,mech_phone,mech_email,mech_address,typeid) 
		update(q)
		return redirect(url_for('admin.admin_manage_mechanic')) 
	if 'add' in request.form:
		mech_name=request.form['company_name']	
		mech_place=request.form['company_place']	
		mech_phone=request.form['company_phone']	
		mech_email=request.form['company_email']	
		mech_address=request.form['company_address']	
		username=request.form['username']	
		password=request.form['password']	
		qin="select * from login where username='%s' or password='%s'"%(username,password)
		ress=select(qin)
		if ress:
			flash("sorry username or password already exists try again")
		else:
			q="insert into login values(null,'%s','%s','mechanic')" %(username,password)     
			res=insert(q) 
			q="insert into mechanics values(null,'%s','%s','%s','%s','%s','%s',curdate())" %(res,mech_name,mech_place,mech_phone,mech_email,mech_address)     
			insert(q) 
			return redirect(url_for('admin.admin_manage_mechanic')) 
	q="select * from mechanics inner join login using(login_id)" 	
	res=select(q) 
	data['type']=res 
	return render_template('admin_manage_mechanic.html',data=data) 

	

@admin.route('/adminviewusers',methods=['get','post']) 
def adminviewusers(): 
	data={}
	if 'action' in request.args:
		action=request.args['action'] 
		userid=request.args['id'] 
	else:
		action=None	

	if action=="approve": 
		q="update login set usertype='users' where login_id='%s'" %(userid)  
		print(q)
		update(q)
		return redirect(url_for('admin.adminviewusers'))
		
	if action=="reject": 
		q="delete from login where login_id='%s'" %(userid)  
		delete(q)
		return redirect(url_for('admin.adminviewusers')) 
		
    	

	q="SELECT * FROM `users` INNER JOIN `login` USING(`login_id`) WHERE `usertype`='pending'"
	   
	res=select(q)
	data['users']=res
	print(res) 	

	return render_template('adminviewusers.html',data=data)  

@admin.route('/adminverifyusers',methods=['get','post']) 
def adminverifyusers(): 
	data={}
	q="SELECT * FROM `users` INNER JOIN `login` USING(`login_id`) WHERE `usertype`='users'" 
	res=select(q)
	data['users']=res 		

	return render_template('adminverifyusers.html',data=data)  	 
@admin.route('/adminviewfeedback',methods=['get','post']) 
def adminviewfeedback(): 
	data={}
	q="select * from feedback INNER JOIN users using(user_id)" 
	res=select(q)
	print(res)
	data['feedback']=res 	
	
	return render_template('adminviewfeedback.html',data=data) 

@admin.route('/adminmanagehotels',methods=['get','post'])  	
def adminmanagehotels():
	data={}
	if 'action' in request.args:
		action=request.args['action'] 
		hotelid=request.args['id'] 
	else:
		action=None
	if action=="delete":
		q="delete from hotels where hotel_id='%s'" %(hotelid)  
		delete(q)
		return redirect(url_for('admin.adminmanagehotels'))  
	
	if 'add' in request.form:
		placeid=request.form['place_id']
		hotel=request.form['hotel'] 
		pincode=request.form['pincode'] 
		q="insert into hotels values(null,'%s','%s','%s')" %(placeid,hotel,pincode)  
		insert(q) 
		return redirect(url_for('admin.adminmanagehotels')) 
	q="select * from hotels INNER JOIN place using(place_id)" 
	res=select(q) 
	data['hotels']=res 	
	q="select * from place"  
	res=select(q) 
	data['place']=res
	return render_template('adminmanagehotels.html',data=data)   

@admin.route('/adminmanagerooms',methods=['get','post'])  	
def adminmanagerooms():
	data={}
	if 'action' in request.args: 
		action=request.args['action'] 
		roomid=request.args['id'] 
	else:
		action=None
	if action=="delete":
		q="delete from rooms where room_id='%s'" %(roomid)  
		delete(q)
		return redirect(url_for('admin.adminmanagerooms'))  
	
	if 'add' in request.form:
		hotelid=request.form['hotel_id']
		roomnumber=request.form['roomnumber'] 
		rate=request.form['rate'] 
		
	 
		q="insert into rooms values(null,'%s','%s','%s')" %(hotelid,roomnumber,rate)  
		insert(q) 
		return redirect(url_for('admin.adminmanagerooms')) 
	
	q="select * from rooms INNER JOIN hotels using(hotel_id)" 	 

	res=select(q)
	data['rooms']=res  
	q="select * from hotels"   
	res=select(q)
	data['hotel_id']=res   
	return render_template('adminmanagerooms.html',data=data) 
	
		
@admin.route('/adminstaffallocate',methods=['get','post']) 
def adminstaffallocate():
	data={}  
	if 'action' in request.args:
		action=request.args['action'] 
		allocateid=request.args['id'] 
	else:
		action=None
	if action=="delete": 
		q="delete from staffallocate where allocate_id='%s'" %(allocateid) 
		delete(q) 
		return redirect(url_for('admin.adminstaffallocate'))	

	if 'submit' in request.form: 
		staffid=request.form['staff_id'] 
		airportid=request.form['airport_id'] 
		q="insert into staffallocate values(null,'%s','%s','accept')" %(staffid,airportid)  
		print(q)
		insert(q) 
		return redirect(url_for('admin.adminstaffallocate')) 

	

	q="select *,CONCAT(`firstname`,' ',`lastname`)as names from staffallocate INNER JOIN staff using(staff_id) INNER JOIN airports using(airport_id)"   
	res=select(q) 
	print(res)
	data['allocate']=res   
	q="select *,CONCAT(`firstname`,' ',`lastname`)as names from staff" 
	res=select(q) 
	data['staff_id']=res 
	q="select * from airports" 
	res=select(q)
	data['airport_id']=res  
	return render_template('adminstaffallocate.html',data=data)   




@admin.route('/view_booking',methods=['get','post'])
def view_booking():
    data={}
    q = "SELECT `ticketsbooked`.*, `flight_schedule`.*,flights.*,passengers.*, `from_airport`.`name` AS `from_airport_name`, `to_airport`.`name` AS `to_airport_name` FROM ticketsbooked INNER JOIN flight_schedule USING(schedule_id)INNER JOIN `airports` AS `from_airport` ON `flight_schedule`.`from_airport_id` = `from_airport`.`airport_id` INNER JOIN `airports` AS `to_airport` ON `flight_schedule`.`to_airport_id` = `to_airport`.`airport_id` INNER JOIN passengers USING(booked_id) INNER JOIN flights USING(flight_id)"
    res = select(q)
    data['ticketsbooked'] = res 
    return render_template('admin_view_booking.html', data=data)



@admin.route('/view_passengers', methods=['GET', 'POST'])
def view_passengers():
    data={}
    bid = request.args['bid'] 
    data['bid'] = bid
    fid = request.args['fid']
    data['fid'] = fid
    q = "SELECT *, CONCAT(first_name, ' ', last_name) AS names FROM passengers WHERE booked_id='%s'" % (bid)
    res = select(q)
    data['passengers'] = res 		
    return render_template('adminviewpassengersdetails.html',data=data)




		

	



	

		



	

	 
	

	