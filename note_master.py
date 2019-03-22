from tkinter import *
from tkinter import ttk

field_value = "Enter tactics and signals here"  # returned from another part of the code

# triggered off left button click on text_field

def copy_text_to_clipboard():
	field_value = signals_field.get(1.0, 'end-1c')  # get field value from event, but remove line return at end
	window.clipboard_clear()  # clear clipboard contents
	window.clipboard_append(field_value)  # append new value to clipbaord

def change_queue(q='bme'):
	# print(q)
	tags = ''
	if q=='Business Enforcement':
		for child in f1.winfo_children():

			r = child.grid_info()['row'] if 'row' in child.grid_info().keys() else 1
			# print(r)
			if ((str(child["state"]) == 'disabled') or (r < 2)):
				print('hello')
				pass
			else:
				# print(child.grid_info())
				row = child.grid_info()['row']+1
				child.grid(row=row)
			# # if ((child.cget("state") == 'disabled') or (child.grid_info()['row'] < 2)):
			# 	print(child.grid_info())
			# 	pass
			# else:
			# 	# col = child.grid_info()['column']
			# 	row = child.grid_info()['row']+1
			#
			# 	child.grid(row=row)

		accts_label.config(state=NORMAL)
		accts_field.config(state=NORMAL)

		accts_label.grid(row=2, column=1, sticky=(W+E))
		accts_field.grid(row=2, column=2, sticky=(W))
		tags = "#BME #ALE"

	else:
		accts_label.config(state=DISABLED)
		accts_field.config(state=DISABLED)
		accts_label.grid_remove()
		accts_field.grid_remove()


		if q=='User Enforcement':
			tags = "#UE #ALE"

		if q=='Business Manager Appeals':
			tags = "#BMA #ALE"

		if q=='User Appeals':
			tags = "#UA #ALE"

	tag_var.set(tags)

def reset():
	accts_var.set("")
	policy_var.set("")
	signals_field.delete(1.0, 'end')

def more_statuses(selection):
	pass


window = Tk()
window.title('Notes')

pw = ttk.Panedwindow(window, orient=HORIZONTAL)
pw.grid(column=0, row=0, sticky=(N,W,E,S))

# setup frame and grid
f1 = ttk.Labelframe(pw, width=320, height=240, text='Frame 1')
# f1.grid(column=0, row=0, sticky=(N, W, E, S))

f2 = ttk.Labelframe(pw, width=320, height=240, text='Preview')
f2.config(borderwidth=3)
print('f2.config', f2.config())
# f1.grid(column=0, row=0, sticky=(N, W, E, S))

pw.add(f1, weight=50)
pw.add(f2, weight=50)

pw.pack(fill='both', expand=True)


# queue_menu.add_command(label='Business Enforcement', command=change_queue)
# queue_menu.add_command(label="Exit", command=window.quit)

# window.config(menu=queue_menu)

# topframe = ttk.Frame(window, padding="3 3 12 12")
# topframe.grid(column=0, row=0, sticky=(N, W, E, S))


# policy_menu = OptionMenu(f1, )

clear_button = ttk.Button(f1, text='clear', command=reset)
clear_button.grid(row=1, column=6, sticky=(E))

accts_var = StringVar()
accts_label = ttk.Label(f1, text="active_accounts", relief=RAISED, state=DISABLED)
accts_field = ttk.Entry(f1, textvariable=accts_var, state=DISABLED)

accts_label.grid(row=2, column=1, sticky=(W+E))
accts_field.grid(row=2, column=2, sticky=(W))

queue_options = ['', 'Business Enforcement', 'User Enforcement',
				'Business Manager Appeals', 'User Appeals']

queue_label = ttk.Label(f1, text='Queue: ', relief=RAISED)
queue_label.grid(row=1, column=1, sticky=(W+E))

queue_var = StringVar()
queue_menu = ttk.OptionMenu(f1, queue_var, *queue_options, command=change_queue)

queue_menu.grid(row=1, column=2, sticky=(W))


policies = ['', 'User Trust', 'LQEC', 'Misleading Merch', 'Cloaking', 'Porn',
			'Illegal', 'Ineligible for review']

policy_var = StringVar()
policy_violation_menu = ttk.OptionMenu(f1, policy_var, *policies)
policy_violation_menu.grid(row=2, column=2, sticky=(N, W), padx=1, pady=1)

policy_label = ttk.Label(f1, relief=RAISED, text='POLICY VIOLATION:')
policy_label.grid(row=2, column=1, sticky=(N, W+E))

ad_ids_label = ttk.Label(f1, relief=RAISED, text='AD IDs:')
ad_ids_label.grid(row=3, column=1, sticky=(W+E))

ads_var = StringVar()
ad_ids_field = ttk.Entry(f1, textvariable=ads_var)
ad_ids_field.grid(row=3, column=2, sticky=(W))

# setup our inline label and widget
# ad_ids_field = Entry(frame, )

signals_field = Text(f1, width=60, maxundo=5)
signals_field.insert(1.0, field_value)
signals_field.grid(row=4, column=2, sticky=(N), columnspan=6)

signals_label = ttk.Label(f1, text="SIGNALS:", relief=RAISED)
signals_label.grid(row=4, column=1, sticky=(N, W+E))

acct_status_options = ['ADS_INTEGRITY_POLICY', 'BI_RAR', 'Business Banhammered',
				'BUSINESS_INTEGRITY_RAR','ADS_AFC_REVIEW', 'ADS_IP_REVIEW',
				'RISK_PAYMENT', "Hasn't Run Ads", 'Closed', 'PERMANENT_CLOSE',
				'Has Run Ads', 'Unsettled', 'UNUSED_ACCOUNT',
				'GRAY_ACCOUNT_SHUTDOWN', 'None']

acct_status_var = StringVar()

breakdown_label = ttk.Label(f1, text="ACCOUNT BREAKDOWN:", relief=RAISED)
breakdown_field = ttk.OptionMenu(f1, acct_status_var, *acct_status_options, command=more_statuses)

breakdown_field['menu'].insert(8, "separator")
breakdown_field['menu'].insert(11, "separator")
# print(breakdown_field.keys())
# breakdown_field.add_separator(text='Active')

breakdown_label.grid(row=5, column=1)
breakdown_field.grid(row=5, column=2, sticky=(W), padx=1, pady=1)

numvar = IntVar()
number_box = Spinbox(f1, from_=1, to=10000, textvariable=numvar, width=5)
number_box.grid(row=5, column=3, sticky=(W))

copy_button = ttk.Button(f1, text='copy', command=copy_text_to_clipboard)
copy_button.grid(row=5, column=6)

# breakdown_field.bind('<<ComboboxSelected>>', more_statuses)

tag_var = StringVar()
tags_field = ttk.Label(f1, textvariable=tag_var)
tags_field.grid(row=6, column=2, sticky=(W))

tags_label = ttk.Label(f1, text='Tags:', relief=RAISED)
tags_label.grid(row=6, column=1, sticky=(W+E))


#preview pane frames/widgets

#policy violation frame
pv_prev_frame = ttk.Frame(f2)
pv_prev_frame.grid(row=1, column=0, sticky=(W))

policy_viol_label_prev = ttk.Label(pv_prev_frame, text='POLICY VIOLATION: ')
policy_viol_label_prev.grid(row=0, column=0, sticky=(W))

policy_viol_field_prev = ttk.Label(pv_prev_frame, textvariable=policy_var)
policy_viol_field_prev.grid(row=0, column=1, sticky=(W))

#ad IDs frame
ad_ids_frame = ttk.Frame(f2)
ad_ids_frame.grid(row=2, column=0, sticky=(W))

ad_ids_prev_label = ttk.Label(ad_ids_frame, text='AD IDs:')
ad_ids_prev_label.grid(row=0, column=0, sticky=(W))

ad_ids_field = ttk.Label(ad_ids_frame, textvariable=ads_var)
ad_ids_field.grid(row=0, column=1, sticky=(W))

#signals frame
signals_frame = ttk.Frame(f2)
signals_frame.grid(row=3, column=0, sticky=(W))

signals_prev_label = ttk.Label(signals_frame, text='SIGNALS:')
signals_prev_label.grid(row=0, column=0, sticky=(W, N))

signals_prev_field = Text(signals_frame, width=40, height=20)
signals_prev_field.insert(1.0, field_value)
signals_prev_field.grid(row=0, column=1, sticky=(W))
signals_prev_field.config(state=DISABLED)

# breakdown_prev_label = ttk.Label(f2, text='ACCOUNT BREAKDOWN:')
# breakdown_prev_label.grid(row=4, column=1, sticky=(W))

# account breakdown frame
breakdown_frame = ttk.Frame(f2)
breakdown_frame.grid(row=4, column=0, sticky=(W))

breakdown_prev_label = ttk.Label(breakdown_frame, text='ACCOUNT BREAKDOWN:')
breakdown_prev_label.grid(row=0, column=0, sticky=(W))

breakdown_prev_field = ttk.Label(breakdown_frame, textvariable=acct_status_var)
breakdown_prev_field.grid(row=0, column=1, sticky=(W))

tags_prev_field = ttk.Label(breakdown_frame, textvariable=tag_var)
tags_prev_field.grid(sticky=(W))

# box_label = ttk.Label(frame, text='Test:')
# box_label.grid(row=7, column=1)



# button.bind('<Button-1>')

# Bind left click on text widget to copy_text_to_clipboard() function
# signals_field.bind('<Return>', copy_text_to_clipboard)



# for child in frame.winfo_children():
	# try:
	# 	# print("child: ", child)
	# 	# print("child.keys: ", child.keys())
	# 	print("child.cget(state): ", child.cget("state"))
	# except:
	# 	print("oops...", child)
	# 	print(dir(child))
	# # print("child.grid_info: ", child.grid_location())
	# child.grid_configure(padx=3, pady=3)


accts_label.grid_remove()
accts_field.grid_remove()

window.mainloop()

# for x in range(acct_status_options):
