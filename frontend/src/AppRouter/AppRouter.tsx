import { createBrowserRouter, RouterProvider } from "react-router-dom";

import Index from "../pages/Index";
import Game from "../pages/Game";



const routes = [
    {
        path: '/',
        element: <Index />,
    },

    {
        path: 'game/:gameId',
        element: <Game />,
    }
]

const router = createBrowserRouter(routes)

const AppRouter = () => {
    return (
        <RouterProvider router={router} />
    )
}

export default AppRouter;