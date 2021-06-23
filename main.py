import speedtest as st
import tkinter as tk

window = tk.Tk()
window.title("Speed Test")
window.geometry("400x200")


def func_speed_test():
    speed_test = st.Speedtest()
    decimal_download_speed = speed_test.download()
    decimal_upload_speed = speed_test.upload()
    download_speed = round(decimal_upload_speed / (10**6), 2)
    upload_speed = round(decimal_upload_speed / (10**6), 2)
    download_label.config(text="Download speed :"+" "+str(download_speed)+"Mbps")
    upload_label.config(text="Upload speed :"+" "+str(upload_speed)+"Mbps")

button = tk.Button(window, text="Test your internet connection", command=func_speed_test, bg="grey", fg="white", width=30)
button.pack(pady=20)

download_label = tk.Label(window, text="")
download_label.pack()
upload_label = tk.Label(window, text="")
upload_label.pack()

if __name__ == '__main__':
    window.mainloop()


