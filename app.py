import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def submit():
    file_name = file_name_entry.get()
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()
    
    # 简单的时间格式验证
    try:
        start_hour, start_minute, start_second = map(int, start_time.split(':'))
        end_hour, end_minute, end_second = map(int, end_time.split(':'))
        
        # 确保时间格式正确
        if (0 <= start_hour < 24 and 0 <= start_minute < 60 and 0 <= start_second < 60 and
            0 <= end_hour < 24 and 0 <= end_minute < 60 and 0 <= end_second < 60):
            
            # 构建ffmpeg命令
            input_file = f"{file_name}.mp4"
            output_file = f"{file_name}-cap.mp4"
            ffmpeg_command = (
                f"D:\\ffmpeg\\ffmpeg.exe -i {input_file} -q 0 -ss {start_time} -to {end_time} {output_file}"
            )
            
            # 执行ffmpeg命令
            try:
                subprocess.run(ffmpeg_command, shell=True, check=True)
                messagebox.showinfo("成功", f"视频裁剪完成: {output_file}")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("错误", f"ffmpeg命令执行失败: {e}")
        else:
            raise ValueError
    except ValueError:
        messagebox.showerror("输入错误", "时间格式无效，请使用 HH:MM:SS 格式")

# 创建主窗口
root = tk.Tk()
root.title("视频裁剪程序")

# 文件名输入框
tk.Label(root, text="文件名 (不包括扩展名):").grid(row=0, column=0, padx=10, pady=5)
file_name_entry = tk.Entry(root)
file_name_entry.grid(row=0, column=1, padx=10, pady=5)

# 开始时间输入框
tk.Label(root, text="开始时间 (HH:MM:SS):").grid(row=1, column=0, padx=10, pady=5)
start_time_entry = tk.Entry(root)
start_time_entry.grid(row=1, column=1, padx=10, pady=5)

# 结束时间输入框
tk.Label(root, text="结束时间 (HH:MM:SS):").grid(row=2, column=0, padx=10, pady=5)
end_time_entry = tk.Entry(root)
end_time_entry.grid(row=2, column=1, padx=10, pady=5)

# 提交按钮
submit_button = tk.Button(root, text="提交", command=submit)
submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# 运行主事件循环
root.mainloop()
