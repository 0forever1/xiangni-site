import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # 优先使用查询参数 ?to=NAME，也接受 POST 表单提交
    name = request.values.get("to", "") or ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
    return render_template("index.html", name=name)

if __name__ == "__main__":
    # 本地运行：监听所有地址，端口可由环境变量 PORT 指定（方便部署）
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("FLASK_DEBUG", "0") == "1")
