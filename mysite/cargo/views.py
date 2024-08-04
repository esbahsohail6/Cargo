from django.shortcuts import render,redirect
from django.db import connection
from django.http import HttpResponse

from .forms import UpdateForm,NCUSTForm,CardataForm,CarForm,CustForm,login,NICForm,Supplier,modelForm,suppnameform,SalesForm,YearSelectionForm,CustdataForm,Profit
from .models import Car,sales,Deal,Record
from django.db.models import OuterRef,Subquery

# Create your views here.
def dashboard(request):
    loginform=login()
    return render(request,'cargo/login.html',{'loginform':loginform})
    # x=True
    # return render(request,'cargo/index.html',{'x':x})

def handlelogin(request):
    if request.method=="POST":
        CEO_post=None
        manager_post=None
        emp_post=None
        name=request.POST.get('name')
        password=request.POST.get('password')
        query = "SELECT post FROM cargo_user WHERE name = %s AND password=%s "
        with connection.cursor() as cursor:
            cursor.execute(query,[name,password])
            row=cursor.fetchone()
            post=row[0]
            if post=='CEO':
                CEO_post=True
            if post=='Manager':
                manager_post=True
            if post=='Employee':
                emp_post=True
        return render(request,'cargo/index.html',{'CEO_post':CEO_post,'emp_post':emp_post,'manager_post':manager_post})

def data_entry(request):
    car_form=None
    NICform=None
    supp_name_form=None
    Profit_form=None
    if request.method=='POST':
        if 'button' in request.POST:
            button=request.POST.get('button')
            if button=='Enter Car':
                car_form=CarForm()
            if button=='Enter Customer': 
                NICform=NICForm()
            if button=='Enter Supplier':
                supp_name_form=suppnameform()
            if button=='Enter Profit':
                Profit_form=Profit()
    return render(request, 'cargo/data_entry.html',{'car_form':car_form,'NICform':NICform,'Profit_form':Profit_form,'supp_name_form':supp_name_form})

def savecar(request):
    if request.method=="POST":
        model_name=request.POST.get('model_name')
        release_year=request.POST.get('release_year')
        body_style=request.POST.get('body_style')
        transmission=request.POST.get('transmission')
        mileage=request.POST.get('mileage')
        seating_capacity=request.POST.get('seating_capacity')
        cargo_capacity=request.POST.get('cargo_capacity')
        car_dimension=request.POST.get('car_dimension')
        tyre_strength=request.POST.get('tyre_strength')
        color=request.POST.get('color')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        query = """
            INSERT INTO cargo_car (model_name, release_year, body_style, transmission, mileage, seating_capacity, cargo_capacity, car_dimension, tyre_strength, color, price, quantity) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
                # Execute the SQL query
        with connection.cursor() as cursor:
            cursor.execute(query, [model_name, release_year, body_style, transmission, mileage, seating_capacity, cargo_capacity, car_dimension, tyre_strength, color, price, quantity])
        if connection.connection:
            connection.close()
        return redirect('data_entry')

def checkNIC(request):
    if request.method == 'POST':
        modelform=None
        nic_number = request.POST.get('NIC')
        customeri=None
        query = "SELECT id FROM cargo_custform WHERE NIC = %s"
        with connection.cursor() as cursor:
            cursor.execute(query, [nic_number])
            row = cursor.fetchone()
            if connection.connection:
                connection.close()
        
            if row:
                cust_id = row[0]
                modelform=modelForm()
                return render(request, 'cargo/data_entry.html', {'modelform': modelform})
                # Perform further actions if needed using cust_id
            else:
                # NIC does not exist, render the form for new customer entry
                custform=CustForm()
                return render(request, 'cargo/data_entry.html', {'custform': custform})
        



def savecust(request):
    if request.method=="POST":
        modelform=None
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        phone_no=request.POST.get('phone_no')
        email=request.POST.get('email')
        address=request.POST.get('address')
        NIC=request.POST.get('NIC')
        cust_id=None
        request.session['f_name']=f_name
        request.session['email']=email
        query = """
            INSERT INTO cargo_custform (f_name, l_name, phone_no, email, address, NIC) 
            VALUES (%s, %s, %s, %s, %s, %s);
            """
                # Execute the SQL query
        with connection.cursor() as cursor:
            cursor.execute(query, [f_name, l_name, phone_no, email, address, NIC])
            query2 = "SELECT id FROM cargo_custform WHERE f_name = %s"
            cursor.execute(query2,[f_name])
            row_cust=cursor.fetchone()

            cust_id=row_cust[0]
            modelform=modelForm()
        if connection.connection:
            connection.close()
        # This will clear the session and delete the session cookie
        request.session.flush()

        return render(request, 'cargo/data_entry.html', {'modelform': modelform})

        
def checkmodel(request):
    if request.method == 'POST':
        suppname_form = None
        noqt=None
        noqt_modelform=None
        cust_name=request.POST.get('f_name')
        model_name = request.POST.get('model_name')
        release_year = request.POST.get('release_year')
        request.session['model_name']=model_name
        request.session['release_year']=release_year
        query = "SELECT id, quantity, price FROM cargo_car WHERE model_name = %s AND release_year = %s"
        with connection.cursor() as cursor:
            cursor.execute(query, [model_name, release_year])
            row = cursor.fetchone()
            
            if row:
                car_id, quantity, price = row
                new_quantity = max(quantity - 1, 0)  # Ensure quantity is not negative
                # Update the quantity in the database
                if new_quantity==0:
                    
                    noqt=True
                    noqt_modelform=modelForm()
                else:
                    update_query = "UPDATE cargo_car SET quantity = %s WHERE id = %s"
                    cursor.execute(update_query, [new_quantity, car_id])
                    
                    suppname_form = suppnameform()
        if connection.connection:
                connection.close()
        request.session.flush()
        
        return render(request, 'cargo/data_entry.html', {'suppname_form': suppname_form,'noqt':noqt,'noqt_modelform':noqt_modelform})


    
                

    

    
def checksupp(request):
    if request.method == 'POST':
        supp_name = request.POST.get('supp_name')
        supp_address = request.POST.get('supp_address')
        request.session['supp_name']=supp_name
        request.session['supp_address']=supp_address
        query = "SELECT id FROM cargo_supplier WHERE supp_name = %s AND supp_address = %s"
        query_cust = "SELECT id FROM cargo_custform WHERE f_name = %s"
        query_car = "SELECT id,price FROM cargo_car WHERE model_name = %s AND release_year = %s"
        query_sales = """
                INSERT INTO cargo_sales (car_id_id,supplier_id_id,cust_id_id,price)
                VALUES (%s,%s,%s,%s);
                """
        with connection.cursor() as cursor:
            cursor.execute(query, [supp_name, supp_address])
            row = cursor.fetchone()
            if row:
                supp_id = row[0]  # Retrieving supplier ID from the fetched row
            else:
                # Supplier with provided name and address does not exist
                pass
        if connection.connection:
            connection.close()
        request.session.flush()
        return render(request, 'cargo/data_entry.html', {'row': row})

def sales_save(request):
    f_name=request.session.get('f_name')
    email=request.session.get('email')
    model_name=request.session.get('model_name')
    release_year=request.session.get('release_year')
    supp_name=request.session.get('supp_name')
    supp_address=request.session.get('supp_address')
    query_supp = "SELECT id FROM cargo_supplier WHERE supp_name = %s AND supp_address = %s"
    query_cust = "SELECT id FROM cargo_custform WHERE f_name = %s AND email = %s"
    query_car = "SELECT id,price FROM cargo_car WHERE model_name = %s AND release_year = %s"
    query_sales = """
            INSERT INTO cargo_sales (car_id_id,supplier_id_id,cust_id_id,price)
            VALUES (%s,%s,%s,%s);
            """
    with connection.cursor() as cursor:
        cursor.execute(query_supp, [supp_name, supp_address])
        row = cursor.fetchone()
        if row:
            supp_id = row[0]  # Retrieving supplier ID from the fetched row
            cursor.execute(query_car, [model_name,release_year])
            row_car=cursor.fetchone()
            if row_car:
                car_id, price = row_car
                cursor.execute(query_cust, [f_name,email])
                row_cust=cursor.fetchone()
                if row_cust:
                    cust_id = row_cust[0]
                    cursor.execute(query_sales,[car_id, supp_id, cust_id, price])
    if connection.connection:
            connection.close() 
    request.session.flush()   
    return redirect('data_entry')




def suppdatacheck(request):
    if request.method == 'POST':
        modeldataform=None
        supp_form=None
        supp_name = request.POST.get('supp_name')
        supp_address = request.POST.get('supp_address')
        request.session['supp_name']=supp_name
        request.session['supp_address']=supp_address
        query = "SELECT id FROM cargo_supplier WHERE supp_name = %s AND supp_address = %s"
        with connection.cursor() as cursor:
            cursor.execute(query, [supp_name, supp_address])
            row = cursor.fetchone()
            if connection.connection:
                connection.close()
            request.session.flush()
            if row:
                supp_id = row[0]  # Retrieving supplier ID from the fetched row
                modeldataform=modelForm()
                return render(request, 'cargo/data_entry.html',{'modeldataform':modeldataform})
                # Perform further actions if needed using supp_id
            else:
                supp_form=Supplier()
                return render(request, 'cargo/data_entry.html', {'supp_form': supp_form})
        
def checkmodeldataform(request):
    if request.method == 'POST':
        model_name = request.POST.get('model_name')
        release_year = request.POST.get('release_year')
        request.session['model_name']=model_name
        request.session['release_year']=release_year
        query = "SELECT id FROM cargo_car WHERE model_name = %s AND release_year = %s"
        with connection.cursor() as cursor:
            cursor.execute(query, [model_name, release_year])
            row_supp = cursor.fetchone()
            if row_supp:
                car_id=row_supp[0]
            else:
                pass
            if connection.connection:
                connection.close()
            request.session.flush()
            return render(request, 'cargo/data_entry.html', {'row_supp': row_supp})
        
def deals_save(request):
    model_name=request.session.get('model_name')
    release_year=request.session.get('release_year')
    supp_name=request.session.get('supp_name')
    supp_address=request.session.get('supp_address')
    query_supp = "SELECT id FROM cargo_supplier WHERE supp_name = %s AND supp_address = %s"
    query_car = "SELECT id FROM cargo_car WHERE model_name = %s AND release_year = %s"
    query_deal = """
            INSERT INTO cargo_deal (car_id_id,supplier_id_id)
            VALUES (%s,%s);
            """
    with connection.cursor() as cursor:
        cursor.execute(query_supp, [supp_name, supp_address])
        row = cursor.fetchone()
        if row:
            supp_id = row[0]  # Retrieving supplier ID from the fetched row
            cursor.execute(query_car, [model_name,release_year])
            row_car=cursor.fetchone()
            if row_car:
                car_id= row_car[0]
                cursor.execute(query_deal,[car_id,supp_id])
    if connection.connection:
        connection.close()    
    request.session.flush()
    return redirect('data_entry')



def savesupp(request):
    if request.method=="POST":
        modeldataform=None
        supp_name=request.POST.get('supp_name')
        supp_email=request.POST.get('supp_email')
        supp_address=request.POST.get('supp_address')
        supp_phoneno=request.POST.get('supp_phoneno')
        query = """
            INSERT INTO cargo_Supplier (supp_name, supp_email, supp_address, supp_phoneno) 
            VALUES (%s, %s, %s, %s);
            """
                # Execute the SQL query
        with connection.cursor() as cursor:
            cursor.execute(query, [supp_name, supp_email, supp_address, supp_phoneno])
            modeldataform=modelForm()
        if connection.connection:
            connection.close()
        return render(request, 'cargo/data_entry.html', {'modeldataform': modeldataform})


def saveprofit(request):
    if request.method=="POST":
        model_name=request.POST.get('model_name')
        year=request.POST.get('year')
        profit=request.POST.get('profit')
        query = """
            INSERT INTO cargo_profit (model_name, year, profit) 
            VALUES (%s, %s, %s);
            """
        with connection.cursor() as cursor:
            cursor.execute(query, [model_name, year, profit])
        if connection.connection:
            connection.close()
        return redirect('data_entry')



def view_data(request):
    year_select=None
    year_sel=None
    customer_modelName=None
    carData=None
    AllCustData=None
    AllSupplierData=None
    profit=None
    supp=None
    NFound=None

    if request.method=='POST':

        if 'button' in request.POST:
            button=request.POST.get('button')
            if button=='View Sold Car Data':
                year_select=YearSelectionForm()
            if button=='View Supplier Data':
                supp=CardataForm()
            if button=='View Unsold Car Data': 
                year_sel=YearSelectionForm()
            if button=='View Customer Data':
                customer_modelName=CustdataForm()
            if button=='View Car Data':
                carData=CardataForm()
            if button=='View All customer data':
                
                query= """
                      SELECT *
                      FROM cargo_custform
    
            
                      """
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    AllCustData=cursor.fetchall()
                if connection.connection:
                    connection.close()
                if not AllCustData:
                    NFound=True
            if button=='View All supplier data':
                
                query= """
                      SELECT *
                      FROM cargo_supplier
    
            
                      """
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    AllSupplierData=cursor.fetchall()
                if connection.connection:
                    connection.close()
                if not AllSupplierData:
                    NFound=True
            if button=='View Profit':
                
                query= """
                      SELECT *
                      FROM cargo_profit
    
            
                      """
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    profit=cursor.fetchall()
                if connection.connection:
                    connection.close()
                if not profit:
                    NFound=True
    return render(request, 'cargo/view_data.html',{'NFound':NFound,'supp':supp,'profit':profit,'AllSupplierData':AllSupplierData,'AllCustData':AllCustData,'year_select':year_select,'year_sel':year_sel,'customer_modelName':customer_modelName,'carData':carData})
             
def soldcar(request):
    SoldCar_data=None
    year=None
    NFound=False
    if request.method == 'POST':
        year=request.POST.get('year')
        query="""
            SELECT cargo_car.model_name,cargo_car.release_year,cargo_car.price,cargo_sales.cust_id_id
            FROM cargo_car
            JOIN cargo_sales
            ON cargo_car.id=cargo_sales.car_id_id and cargo_car.release_year=%s
            """
        with connection.cursor() as cursor:
            cursor.execute(query,[year])
            SoldCar_data=cursor.fetchall()
        if connection.connection:
            connection.close()
        if not SoldCar_data:
            NFound=True

    return render(request,'cargo/view_data.html',{'NFound':NFound,'SoldCar_data':SoldCar_data})

def unsoldcar(request):
    UnSoldCar_data=None
    year=None
    NFound=False
    if request.method == 'POST':
        year=request.POST.get('year')
        query="""
            SELECT cargo_car.model_name,cargo_car.release_year,cargo_car.price,cargo_car.id
            FROM cargo_car where cargo_car.release_year=%s and cargo_car.id NOT IN(SELECT cargo_sales.car_id_id FROM cargo_sales)
            
            
            """
        with connection.cursor() as cursor:
            cursor.execute(query,[year])
            UnSoldCar_data=cursor.fetchall()
        if connection.connection:
            connection.close()
    if not UnSoldCar_data:
        NFound=True
    return render(request,'cargo/view_data.html',{'NFound':NFound,'UnSoldCar_data':UnSoldCar_data})

def custdata(request):
    Cust_data=None
    NFound=False
    
    if request.method == 'POST':
        Cusmodel=request.POST.get('Enter_Model_Name')
        query="""
              SELECT cargo_custform.f_name,cargo_custform.l_name,cargo_custform.phone_no,cargo_custform.address,cargo_custform.NIC
              FROM cargo_custform JOIN cargo_sales ON cargo_custform.id=cargo_sales.cust_id_id JOIN cargo_car ON cargo_car.id=cargo_sales.car_id_id
              Where cargo_car.model_name=%s
              """
                
        with connection.cursor() as cursor:
            cursor.execute(query,[Cusmodel])
            Cust_data=cursor.fetchall()
        if connection.connection:
            connection.close()
        if not Cust_data:
            NFound=True
            
    return render(request,'cargo/view_data.html',{'NFound':NFound,'Cust_data':Cust_data})


def carinfo(request):
    carinfo=None
    NFound=None
    if request.method == 'POST':
        car_name=request.POST.get('Enter_Car_Model')
        car_year=request.POST.get('Enter_release_Year')
        query="""
              SELECT *
              FROM cargo_car
    
              Where cargo_car.model_name=%s and cargo_car.release_year=%s
              """
        with connection.cursor() as cursor:
            cursor.execute(query,[car_name,car_year])
            carinfo=cursor.fetchall()
        if connection.connection:
            connection.close()
        if not carinfo:
            NFound=True
            
    return render(request,'cargo/view_data.html',{'NFound':NFound,'carinfo':carinfo})

def suppinfo(request):
    S_data=None
    NFound=False
    if request.method == 'POST':
        model = request.POST.get('Enter_Car_Model')
        Ryear = request.POST.get('Enter_release_Year')
    
        query = """
              SELECT cargo_supplier.supp_name,
              cargo_supplier.supp_phoneno,
              cargo_supplier.supp_address,
              cargo_supplier.supp_email
              FROM cargo_supplier
              JOIN cargo_deal ON cargo_supplier.id = cargo_deal.supplier_id_id
              JOIN cargo_car ON cargo_deal.car_id_id = cargo_car.id
              WHERE cargo_car.model_name = %s AND cargo_car.release_year = %s;
            """

        with connection.cursor() as cursor:
            cursor.execute(query, [model,Ryear])
            S_data = cursor.fetchall()
        if connection.connection:
            connection.close()
        if not S_data:
            NFound=True
    
        
    # Process S_data as needed

    return render(request,'cargo/view_data.html',{'NFound':NFound,'S_data':S_data})
def update_data(request):
    updateForm=UpdateForm()
    return render(request,'cargo/update.html',{'updateForm':updateForm})
def check_cust(request):
    if request.method == 'POST':
        NIC = request.POST.get('NIC')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        modelName = request.POST.get('Enter_Car_Model')
        releaseyear = request.POST.get('Enter_release_Year')
        query1= "SELECT cargo_custform.id FROM cargo_custform WHERE cargo_custform.NIC=%s"
        with connection.cursor() as cursor:
            cursor.execute(query1, [NIC])
            x=cursor.fetchone()
        query = "SELECT cargo_Record.cust_id FROM cargo_Record WHERE cargo_Record.NIC=%s"
        with connection.cursor() as cursor:
            cursor.execute(query, [NIC])
            z = cursor.fetchone()
            if z:
                Newcust = NCUSTForm(initial={'cust_id': z[0]})  # Pass the customer ID
                return render(request, 'cargo/delete.html', {'Newcust': Newcust})
            if not z:
                Ncust=NCUSTForm(initial={'cust_id': x[0],'releaseyear':releaseyear,'modelName':modelName,'NIC':NIC,'f_name':f_name,'l_name':l_name})  # Pass the customer ID
                return render(request, 'cargo/update.html', {'Ncust': Ncust})
                
def update_cust(request):
    if request.method == 'POST':
        NCNIC = request.POST.get('New_Customer_NIC')
        NCname = request.POST.get('New_Customer_Name')
        cust_id = request.POST.get('cust_id')  # Ensure the cust_id is passed from the form
        query = """UPDATE cargo_Record SET NewCustomer_name = %s, 
                   NewCustomer_NIC = %s WHERE cust_id = %s"""
        with connection.cursor() as cursor:
            cursor.execute(query, [NCname, NCNIC, cust_id])
    return redirect('dashboard')


def I_cust(request):
        if request.method=='POST':
            NCNIC=request.POST.get('New_Customer_NIC')
            NCname=request.POST.get('New_Customer_Name')
            cust_id = request.POST.get('cust_id')
            NIC = request.POST.get('NIC')
            f_name = request.POST.get('f_name')
            l_name = request.POST.get('l_name')
            modelName = request.POST.get('modelName')
            releaseyear = request.POST.get('releaseyear')

            query="""
            INSERT INTO cargo_Record (NIC, f_name, l_name,NewCustomer_name,NewCustomer_NIC,model_name,release_year,cust_id) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """
            with connection.cursor() as cursor:
                cursor.execute(query,[NIC,f_name,l_name,NCname,NCNIC,modelName,releaseyear,cust_id])
        return redirect('dashboard')


