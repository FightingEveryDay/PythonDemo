from flask import Flask, jsonify, request, abort, Response
from time import time
from uuid import uuid4

app = Flask(__name__)

@app.route('/')
def h():
    return jsonify(statu = 200)

@app.route('/index')
def helloword():
    return jsonify(msg = 'hello word')

class Todo(object):
    def __init__(self, content):
        self.id = str(uuid4())
        self.content = content # todo 内容
        self.create_at = time() # 创建时间
        self.is_finished = False # 是否完成
        self.finished_at = None # 完成时间

    def finish(self):
        self.is_finished = True
        self.finished_at = time()

    def json(self):
        return {
            'id':self.id,
            'content':self.content,
            'create_at':self.create_at,
            'is_finished':self.is_finished,
            'finished_at':self.finished_at
        }

todos = {}
get_todo = lambda tid: todos.get(tid, False)

@app.route('/todo')
def index():
    return jsonify(data=[todo.json() for todo in todos.values()])

@app.route('/todo', methods=['POST'])
def add():
    print(str(request))
    content = request.form.get('content', 'aaa')
    if not content:
        abort(400)
    todo = Todo(content)
    todos[todo.id] = todo
    print(todos.values())
    return jsonify(data = [todo.json() for todo in todos.values()])
    # return jsonify(todo.json())
    # print(str(Response(todo)))
    # return Response(todos)

@app.route('/todo/<tid>/finish', methods=['PUT', 'POST'])
def finish(tid):
    todo = get_todo(tid)
    if todo:
        todo.finish()
        return jsonify(data = [t.json() for t in todos.values()])
    abort(404)

@app.route('/todo/<tid>/del', methods=['DELETE', 'POST'])
def delete(tid):
    todo = get_todo(tid)
    if todo is True:
        todos.pop(tid)
        return jsonify(result = True,data = [t.json() for t in todos.values()])
    else:
        return jsonify(result = False, msg = '错误,找不到对象')

def test_run():
    print('hello word')

if __name__ == '__main__':
    test_run()
    app.run(host='127.0.0.1', port=8080)
