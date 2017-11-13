render
======

.. js:function:: render()

    Рендерит react элемент в дом дерево

    .. code-block:: js

        ReactDom.render(
            React.createElement('h2', null, 'Hello World'),
            document.getElementById('root')
        );

        // jsx
        ReactDom.render(
            <h2>Hello World</h2>,
            document.getElementById('root')
        )

    .. code-block:: js

        import App from "./components/App";

        ReactDom.render(<App />, root);

