import flet as ft

class UserInterface:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "یادآور هوشمند تینا"
        self.page.rtl = True
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # تعریف ویجت‌ها و نسبت دادن به self
        self.text=ft.Text("یادآور هوشمند", size=30, weight="bold", color="#007bff")
        self.input_comment = ft.TextField(label="یادآوری", width=300, text_align=ft.TextAlign.RIGHT)
        self.input_date = ft.TextField(label="تاریخ (مثلا 1403/05/01)", width=300, text_align=ft.TextAlign.RIGHT)
        self.input_time = ft.TextField(label="ساعت (مثلا 14:30)", width=300, text_align=ft.TextAlign.RIGHT)
        self.message_label = ft.Text(value="", size=14)
        self.add_button = ft.ElevatedButton("اضافه کردن یادآوری")
        self.delete_handler = None
        self.edit_handler = None
        self.save_edit_handler = None
        # اینها یهنی تا ما کلیک نکرده ایم هیچ کاری انجام ندهند
        self.search_button = ft.ElevatedButton("جستجو کردن یادآوری")
        self.search_handler = None
        
        
        self.reminders_view = ft.Column()
        self.reminders_table = ft.DataTable(
        columns=[
                ft.DataColumn(ft.Text("آیدی")),
                ft.DataColumn(ft.Text("یادآوری")),
                ft.DataColumn(ft.Text("تاریخ")),
                ft.DataColumn(ft.Text("ساعت")),
                ft.DataColumn(ft.Text("وضعیت")),
                ft.DataColumn(ft.Text("عملیات")),
            ],
            rows=[]
        )    
        self.reminders_view.controls.append(
            self.reminders_table
        )
    # این دو تا با هم فرق دارند:self.reminders_tableاین خود جدول است.ولی:self.reminders_viewظرفیه که جدول رو داخلش گذاشتیم.    

        # چیدن اجزا در صفحه
        self.page.add(
            ft.Column(
                [
                    self.text,
                    
                    self.input_comment,

                    self.input_date,

                    self.input_time,

                    self.add_button,
                    
                    self.search_button,

                    self.message_label,
                    
                    self.reminders_view,
                        
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15 ,
                # بین تمامی اعضا یه 15 پیکسلی فاصله باشد 
                scroll=ft.ScrollMode.AUTO,
                expand=True
            )
        )

    def get_inputs(self):
        return self.input_comment.value, self.input_date.value, self.input_time.value
        # مقادیری که توسط کاربر وارد شده را میگیرد
    def clear_inputs(self):
        self.input_comment.value = ""
        self.input_date.value = ""
        self.input_time.value = ""
            
    def set_message(self, message, color):
        self.message_label.value = message
        self.message_label.color = color
        # این در فایل دوم کاردبردش مشخص میشه برای نمایش متن و رنگ پیام ها 
        
    def set_add_button_handler(self, handler):
        # این قسمت مهمه چووونننن تابعی که توسط دکمه اجرا میشود اینجاست 
        self.add_button.on_click = handler
        # واین میگه وقتی دکمه کلیک شد باید یه چی که به جاش من کلمه ی handler گذاشتمو اجرا کنی
    
    def set_search_button_handler(self, handler):
            # این قسمت مهمه چووونننن تابعی که توسط دکمه اجرا میشود اینجاست 
            self.search_button.on_click = handler
     
    def show_reminders(self, reminders):
        for reminder in reminders:
            if reminder[4] == 0:
                status = "انجام نشده"
            else:
                status = "انجام شده"
            row= ft.DataRow(
              cells=[
                ft.DataCell(ft.Text(str(reminder[0]))),
                ft.DataCell(ft.Text(str(reminder[1]))),
                ft.DataCell(ft.Text(str(reminder[2]))),
                ft.DataCell(ft.Text(str(reminder[3]))),
                ft.DataCell(ft.Text(status)),
                ft.DataCell(
                ft.Row(
                    [ft.IconButton(icon=ft.Icons.EDIT,tooltip="ویرایش" , on_click=lambda e, reminder_id=reminder[0]: self.edit_click(reminder_id)),
                     ft.IconButton(icon=ft.Icons.DELETE,tooltip="حذف", on_click=lambda e , reminder_id=reminder[0]: self.delete_click(reminder_id)),
                     ]))   
              ]  
            )
            self.reminders_table.rows.append(row)
            
    def refresh_reminders(self, reminders):
        # همه ی اطلاعات قبلی که اضافه شده بودند را پاک کن و اطلاعات جدید را وارد کن 
        self.reminders_table.rows.clear()
        self.show_reminders(reminders)
            
    # دو تابع پایین می گن وقتی که دکمه کلیک شد بره یه تابع از یه جای دیگه که به دیتابیس وصله را اجرا کند 
    def delete_click(self, id):
        self.delete_handler(id)
  
    def set_delete_handler(self, handler):
        self.delete_handler = handler
        
    def edit_click(self, id):
        self.edit_handler(id)
        
    def set_edit_handler(self, handler):
        self.edit_handler = handler 
        
    def show_edit_dialog(self, reminder):
        # print("اطلاعات برای ویرایش:", reminder)
        # value باعث میشه متن یا هر چیزی داخل فیلد ها قرارب بگریند
        comment_field = ft.TextField(label="یادآوری", value=reminder[1])

        date_field = ft.TextField(label="تاریخ",value=reminder[2])

        time_field = ft.TextField(label="ساعت",value=reminder[3])
        
        status_field = ft.Dropdown(label="وضعیت",width=200,options=[
            ft.dropdown.Option("انجام نشده"),
            ft.dropdown.Option("انجام شده"), 
        ],
        value="انجام شده" if reminder[4] == 1 else "انجام نشده",                          
        )
        
        dialog = ft.AlertDialog(
        title=ft.Text("ویرایش یادآوری"),
        content=ft.Column(
                [
                    comment_field,
                    date_field,
                    time_field,
                    status_field
                ],
                tight=True,
            ),
            actions=[ft.TextButton("ذخیره تغییرات" , on_click=lambda e: self.save_edit(
                reminder[0],
                comment_field,
                date_field,
                time_field,
                status_field,
                dialog
            )),],
        )
        

        self.page.show_dialog(dialog)     
    
    def save_edit(self,id,comment_field,date_field,time_field,status_field,dialog):
        comment = comment_field.value
        date = date_field.value
        time = time_field.value
        if status_field.value == "انجام شده":
            is_done = 1
        else:
            is_done = 0
        self.save_edit_handler(id, comment, date, time,is_done, dialog)
        
    def set_save_edit_handler(self, handler):
        self.save_edit_handler = handler
        
    def show_search_dialog(self):
        result_view = ft.Column()
        id_field=ft.TextField(label="id مورد نظر برای یادآوری را وارد کنید")
        dialog = ft.AlertDialog(
            title=ft.Text("جستجو یادآوری"),
            content=ft.Column(
                    [id_field,result_view],
                    tight=True,
                ),
            actions=[ft.TextButton("جستجو" , on_click=lambda e: self.go_search(
                            id_field,
                            dialog,
                            result_view
                        )),],
        )
        self.page.show_dialog(dialog)
        
    def go_search(self, id_field , dialog , result_view): 
        remider_id = id_field.value
        
        self.search_handler(remider_id, dialog , result_view)  
            
    def set_search_handler(self , handler):
        self.search_handler = handler
        
    def show_search_result(self, reminder, result_view):

        result_view.controls.clear()

        if reminder:

            data = reminder[0]

            table = ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("آیدی")),
                    ft.DataColumn(ft.Text("یادآوری")),
                    ft.DataColumn(ft.Text("تاریخ")),
                    ft.DataColumn(ft.Text("ساعت")),
                    ft.DataColumn(ft.Text("وضعیت")),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(data[0]))),
                            ft.DataCell(ft.Text(str(data[1]))),
                            ft.DataCell(ft.Text(str(data[2]))),
                            ft.DataCell(ft.Text(str(data[3]))),
                            ft.DataCell(
                                ft.Text(
                                    "انجام نشده"
                                    if data[4] == 0
                                    else "انجام شده"
                                )
                            ),
                        ]
                    )
                ],
            )

            result_view.controls.append(table)

        else:
            result_view.controls.append(
                ft.Text("یادآوری مورد نظر پیدا نشد!")
            )

        self.page.update()
        
    def show_info(self):
           
        dialog = ft.AlertDialog(
        content=ft.Container(
            width=500,
            height=400,
            content=ft.Column(
                [
                ft.Text(
                    "معرفی و اطلاعات برنامه",
                    size=30,
                    color="#0E3449",
                    text_align=ft.TextAlign.CENTER,
                    weight="bold"
                ),
                ft.Text(
                    ": سازنده",
                    size=14,
                    color="#777777",
                    text_align=ft.TextAlign.RIGHT,
                ),
                ft.Text(
                    "تینا خضرنژاد",
                    size=22,
                    weight="bold",
                    color="#074CA8",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "09149838328",
                    size=16,
                    color="#555555",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    ": استاد راهنما",
                    size=14,
                    color="#777777",
                    text_align=ft.TextAlign.RIGHT,
                ),
                ft.Text(
                    "جمال عزیزبیگی",
                    size=22,
                    weight="bold",
                    color="#074CA8",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "09149822453",
                    size=16,
                    color="#555555",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    ": آموزشگاه",
                    size=14,
                    color="#777777",
                    text_align=ft.TextAlign.RIGHT,
                ),
                ft.Text(
                    "تفکر نو ",
                    size=22,
                    weight="bold",
                    color="#074CA8",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "آذربایجان غربی - بوکان - کوچه ی بهداشت خیابان یکشوه",
                    size=16,
                    color="#555555",
                    text_align=ft.TextAlign.CENTER,
                ),
                ],
                spacing=8,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            ),
        )
        )
        
        self.page.show_dialog(dialog)
        

def initialize_ui(page: ft.Page):
    return UserInterface(page)
# این یک تابع برای ساخت پنجره است 
