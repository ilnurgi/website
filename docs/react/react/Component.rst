Component
=========

.. code-block:: js

    // components/App.js

    const App = () => {
        return {
            <h2>Hello World</h2>
        };
    };
    export default App;

.. code-block:: js

    import SomeComponent from "./SomeComponent"

    const App = (props) => {
        return {
            <SomeComponent />
            <SomeComponent />
            <div onClick={() => console.log(this, '${props.item}')}>
            </div>
            {props.books.map(book => <Book />)}
        };
    };

.. code-block:: js

    // components/App.js

    import BookList from './components/BookList'

    class App extends React.Component {
        params = {
            myname: "ilnurgi"
        };

        componentDidMount(){
            this.setState({books: some_books_data})
        }
        render() {
            return {
                <h2>Hello World, {this.params.myname}</n>
                <BookList books={this.state.books} />
            };
        };
    };

    export default App;

.. code-block:: js

