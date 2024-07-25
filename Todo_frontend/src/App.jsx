import { useEffect, useState } from "react";
import { IoMdAdd } from "react-icons/io";
import { FaTrashAlt } from "react-icons/fa";
import { FaRegEdit } from "react-icons/fa";
import "./App.css";
import axios from "axios";
import toast from "react-hot-toast";

function App() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState("");
  

  const getTodos = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/v1/todos");
      // console.log(response.data)
      if(response.data && response.data.data && response.data.data.length>0){

        setTodos(response.data.data);
      
      }
      else{
        setTodos([])
        toast.error('todos not found!')
      }
    } catch (error) {
      toast.error("error fetching todos");
    }
  };

  const addTodo = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/v1/todos", {
        task: newTodo,
      });
      if (response) {
        toast.success("new todo added!");
        setTodos([...todos, response.data.data]);
        setNewTodo("");
      } else {
        toast.error("error adding todos!");
      }
    } catch (error) {
      console.log(error);
      toast.error("error adding todos");
    }
  };

  const deleteTodo = async (id) => {
    try {
      const response = await axios.delete(
        `http://127.0.0.1:8000/api/v1/todos/${id}`
      );
      // console.log(response)
      if (response.status == 204) {
        toast.success("todo deleted successfully!");
        setTodos(todos.filter((todo) => todo.id != id));
      }
    } catch (error) {
      console.log(error);
      toast.error("error deleting todos");
    }
  };


  const updateTodo=async(id)=>{
    const response = await axios.patch(`http://127.0.0.1:8000/api/v1/todos/${id}`);
    console.log(response)
    if(response.status ===200){
      toast.success('status updated successfully!')
      setTodos(todos.map((todo)=>todo.id=== id ? {...todo , status : !todo.status} : todo))
    }
  }



  useEffect(() => {
    getTodos();
  }, []);

  return (
    <div className="flex flex-col items-center justify-center bg-[#000000] min-h-32 w-[400px] m-[auto] mt-10 rounded-lg text-white p-4 gap-6 ">
      <div className="flex items-center gap-10 ">
        <div className="font-semibold ">Your Task</div>
        {/* <div className="text-center  ">
          <button className="bg-gray-600  p-1 font-semibold rounded-md">
            Finished
          </button>
          <button className="ml-1 bg-gray-600  p-1 font-semibold rounded-md">
            Remaining
          </button>
        </div> */}
      </div>
      <form className="flex" onSubmit={addTodo}>
        <input
          type="text"
          value={newTodo}
          className="p-1 rounded-sm bg-gray-400 mr-1 outline-none text-green-900 text-xl font-semibold"
          name="mytodo"
          required
          onChange={(e) => setNewTodo(e.target.value)}
        />
        <button className="bg-[#009688] p-1 text-2xl rounded-sm ">
          <IoMdAdd />
        </button>
      </form>
      <hr />
      <div className="flex flex-col gap-4 mb-10">
        {todos.map((todo) => (
          <div
            className="flex items-center justify-between rounded-md   bg-gray-600 h-10 w-[300px] p-2 "
            key={todo.id}
          >
            <h4 className={todo.status ? 'line-through' : ""}>{todo.task}</h4>
            
            <div className="flex items-center justify-center  gap-2">
              <button className="text-2xl" onClick={()=>updateTodo(todo.id)}>
                <FaRegEdit />
              </button>
              <button className="text-xl" onClick={() => deleteTodo(todo.id)}>
                <FaTrashAlt />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
