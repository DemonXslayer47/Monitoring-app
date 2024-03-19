import psutil
import GPUtil
from flask import Flask, render_template

app = Flask(__name__)

def get_gpu_info():
    try:
        gpus = GPUtil.getGPUs()
        gpu_info = []
        for gpu in gpus:
            gpu_info.append({
                'name': gpu.name,
                'usage': gpu.load * 100,
                'memory_total': gpu.memoryTotal,
                'memory_used': gpu.memoryUsed,
                'memory_free': gpu.memoryFree
            })
        return gpu_info
    except Exception as e:
        print(f"Failed to retrieve GPU information: {e}")
        return []

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    cpu_count = psutil.cpu_count()
    ram_percent = psutil.virtual_memory().percent
    total_ram = round(psutil.virtual_memory().total / (1024.0 ** 3), 2)
    
    try:
        rom_usage = psutil.disk_usage('/').percent
    except Exception as e:
        print(f"Failed to retrieve disk usage information: {e}")
        rom_usage = None
    
    wifi_info = psutil.net_if_addrs().get('Wi-Fi', [])
    gpu_info = get_gpu_info()
    
    message = None
    if cpu_percent > 80 or ram_percent > 80 or (rom_usage is not None and rom_usage > 80):
        message = "High CPU, RAM, or ROM usage detected. Consider scaling up!"
    
    return render_template("index.html", cpu_percent=cpu_percent, cpu_count=cpu_count, ram_percent=ram_percent, total_ram=total_ram, rom_percent=rom_usage, wifi_info=wifi_info, gpu_info=gpu_info, message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
