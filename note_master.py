from tkinter import *
from tkinter import ttk
from tkinter import font

signals_field_value = "Enter tactics and signals here"

def copy_text_to_clipboard():
	clips = []
	window.clipboard_clear()  # clear clipboard contents

	if queue_var.get() == 'Business Enforcement':
		clips.append("ale_bm_enforcement_active_accounts("+accts_var.get()+")")

	clips.append("POLICY VIOLATION: "+ policy_var.get())
	clips.append("Ad IDs: " + ads_var.get())
	clips.append("SIGNALS: " + signals_field.get(1.0, 'end-1c'))
	clips.append("ACCOUNT BREAKDOWN: " + acct_status_var.get())
	clips.append(tag_var.get())

	ff = "\n".join(clips)
	window.clipboard_append(ff)

def change_queue(q='User Appeals'):
	tags = ''
	if q=='Business Enforcement':

		accts_label.config(state=NORMAL)
		accts_field.config(state=NORMAL)
		accts_label.grid(row=2, column=0, sticky=(W))
		accts_field.grid(row=2, column=1, sticky=(W))

		accts_prev_frame.grid(row=1, column=0, sticky=(W))
		# accts_prev_label.config(state=NORMAL)
		# accts_prev_field.config(state=NORMAL)
		accts_prev_label.grid(row=0, column=0, sticky=(W))
		accts_prev_field.grid(row=0, column=1, sticky=(W))
		accts_parenth.grid(row=0,column=2, sticky=(W))

		tags = "#BME #ALE"

	else:
		accts_label.config(state=DISABLED)
		accts_field.config(state=DISABLED)
		accts_label.grid_remove()
		accts_field.grid_remove()

		accts_prev_label.config(state=DISABLED)
		accts_prev_field.config(state=DISABLED)

		accts_prev_label.grid_remove()
		accts_prev_field.grid_remove()
		accts_parenth.grid_remove()
		accts_prev_frame.grid_remove()

		if q=='User Enforcement':
			tags = "#UE #ALE"

		if q=='Business Manager Appeals':
			tags = "#BMA #ALE"

		if q=='User Appeals':
			tags = "#UA #ALE"

	tag_var.set(tags)

def reset():
	accts_var.set("")
	ads_var.set("")
	policy_var.set("")
	signals_field.delete(1.0, 'end')
	acct_status_var.set("")
	preview()

def preview():
	signals_field_value = signals_field.get(1.0, 'end-1c')
	signals_prev_field.config(state=NORMAL)
	signals_prev_field.delete(1.0, 'end')
	signals_prev_field.insert(1.0, signals_field_value)
	signals_prev_field.config(state=DISABLED)

fonts = ['AppleGothic', 'Helvetica Neue']
window = Tk()

style = ttk.Style()
style.configure('TButton', foreground="#dcdcdc", background="#333")
style.map('TButton',
			foreground=[('pressed', 'red'), ('active', 'blue')],
			background=[('pressed', 'yellow'), ('active', 'yellow')],
			relief=[('pressed', 'flat')]
			)

default_font = font.Font(family=fonts[0], size=12)
window.option_add("*Font", default_font)


window.config(bg="#333333")
window.title('Notes')

pw = ttk.Panedwindow(window, orient=HORIZONTAL)
pw.grid(column=0, row=0, sticky=(N,W,E,S))

# setup frame and grid
f1 = ttk.Labelframe(pw, width=260, height=210)

f2 = ttk.Labelframe(pw, width=320, height=240, text='Preview')
f2.config(borderwidth=3)

pw.add(f1, weight=50)
pw.add(f2, weight=50)

pw.pack(fill='both', expand=True)

queue_options = ['', 'Business Enforcement', 'User Enforcement',
				'Business Manager Appeals', 'User Appeals']

queue_var = StringVar()
queue_menu = ttk.OptionMenu(f1, queue_var, *queue_options, command=change_queue)
queue_label = ttk.Label(f1, text='Queue')

queue_label.grid(row=1, column=0, sticky=(W+E))
queue_menu.grid(row=1, column=1, sticky=(W))

accts_var = StringVar()
accts_label = ttk.Label(f1, text="active_accounts", state=DISABLED)
accts_field = ttk.Entry(f1, textvariable=accts_var, state=DISABLED)

accts_label.grid(row=2, column=0, sticky=(W+E))
accts_field.grid(row=2, column=1, sticky=(W))

policies = ['', 'User Trust', 'LQEC', 'Misleading Merch', 'Cloaking', 'Porn',
			'Illegal', 'Ineligible for review']

policy_var = StringVar()
policy_label = ttk.Label(f1, text='POLICY VIOLATION')
policy_violation_menu = ttk.OptionMenu(f1, policy_var, *policies)

policy_label.grid(row=3, column=0, sticky=(N, W+E))
policy_violation_menu.grid(row=3, column=1, sticky=(W))

ads_var = StringVar()

ad_ids_label = ttk.Label(f1, text='Ad IDs')
ad_ids_field = ttk.Entry(f1, textvariable=ads_var)

ad_ids_label.grid(row=4, column=0, sticky=(W+E))
ad_ids_field.grid(row=4, column=1, sticky=(W))

signals_label = ttk.Label(f1, text="SIGNALS")
signals_field = Text(f1, width=30, height=15, maxundo=5)

signals_label.grid(row=5, column=0, sticky=(N, W+E))
signals_field.grid(row=5, column=1, sticky=(N))

signals_field.insert(1.0, signals_field_value)

acct_status_var = StringVar()
breakdown_label = ttk.Label(f1, text="ACCOUNT BREAKDOWN")
breakdown_field = ttk.Entry(f1, textvariable=acct_status_var)

breakdown_label.grid(row=6, column=0, sticky=(W+E))
breakdown_field.grid(row=6, column=1, sticky=(W))



tag_var = StringVar()
tags_label = ttk.Label(f1, text='Tags')
tags_field = ttk.Label(f1, textvariable=tag_var)

tags_label.grid(row=7, column=0, sticky=(W))
tags_field.grid(row=7, column=1, sticky=(W))


# buttons frame
btnframe = ttk.Frame(f1)
btnframe.grid(row=8, column=0, sticky=(W), columnspan=2)

copy_button = ttk.Button(btnframe, text='copy', command=copy_text_to_clipboard)
clear_button = ttk.Button(btnframe, text='reset', command=reset)
preview_button = ttk.Button(btnframe, text='preview', command=preview)

copy_button.grid(row=0, column=0, sticky=(W))
clear_button.grid(row=0, column=1, sticky=(E))
preview_button.grid(row=0, column=2)


#################################
## preview pane frames/widgets ##

#accounts preview frame
accts_prev_frame = ttk.Frame(f2)
accts_prev_frame.grid(row=1, column=0, sticky=(W))

accts_prev_label = ttk.Label(accts_prev_frame, text="ale_bm_enforcement_active_accounts(", state=DISABLED)
accts_prev_field = ttk.Label(accts_prev_frame, textvariable=accts_var)

accts_prev_label.grid(row=0, column=0, sticky=(W))
accts_prev_field.grid(row=0, column=1, sticky=(W))

accts_parenth = ttk.Label(accts_prev_frame, text=")")
accts_parenth.grid(row=0, column=2, sticky=(W))

#policy violation frame
pv_prev_frame = ttk.Frame(f2)
pv_prev_frame.grid(row=2, column=0, sticky=(W))

policy_viol_label_prev = ttk.Label(pv_prev_frame, text='POLICY VIOLATION:')
policy_viol_field_prev = ttk.Label(pv_prev_frame, textvariable=policy_var)

policy_viol_label_prev.grid(row=0, column=0, sticky=(W))
policy_viol_field_prev.grid(row=0, column=1, sticky=(W))

#ad IDs frame
ad_ids_frame = ttk.Frame(f2)
ad_ids_frame.grid(row=3, column=0, sticky=(W))

ad_ids_prev_label = ttk.Label(ad_ids_frame, text='AD IDs:')
ad_ids_field = ttk.Label(ad_ids_frame, textvariable=ads_var)

ad_ids_prev_label.grid(row=0, column=0, sticky=(W))
ad_ids_field.grid(row=0, column=1, sticky=(W))

#signals frame
signals_frame = ttk.Frame(f2)
signals_frame.grid(row=4, column=0, sticky=(W))

signals_prev_label = ttk.Label(signals_frame, text='SIGNALS:')
signals_prev_field = Text(signals_frame, width=30, height=15)

signals_prev_label.grid(row=0, column=0, sticky=(W, N))
signals_prev_field.grid(row=0, column=1, sticky=(W))

signals_prev_field.insert(1.0, signals_field_value)
signals_prev_field.config(state=DISABLED)


# account breakdown frame
breakdown_frame = ttk.Frame(f2)
breakdown_frame.grid(row=5, column=0, sticky=(W))

breakdown_prev_label = ttk.Label(breakdown_frame, text='ACCOUNT BREAKDOWN:')
breakdown_prev_field = ttk.Label(breakdown_frame, textvariable=acct_status_var)

breakdown_prev_label.grid(row=0, column=0, sticky=(W))
breakdown_prev_field.grid(row=0, column=1, sticky=(W))

tags_prev_field = ttk.Label(breakdown_frame, textvariable=tag_var)
tags_prev_field.grid(sticky=(W))


accts_label.grid_remove()
accts_field.grid_remove()

accts_prev_label.grid_remove()
accts_prev_field.grid_remove()
accts_parenth.grid_remove()

window.mainloop()
