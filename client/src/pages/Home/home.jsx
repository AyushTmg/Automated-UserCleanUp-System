import Header from '../../components/Header/header';

export default function Home() {
    return (
        <>
            <Header />
            <div style={{
                paddingTop: '12rem',
                paddingBottom: '1rem',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center'
                }}>
                <div className="p-6 max-w-2xl w-full text-center">
                    <h1 className="text-3xl font-bold mb-4">
                        Hello, I'm Ayush Tamanag aka AT 👋
                    </h1>
                    <p className="text-lg mb-6">
                        Welcome to my personal dashboard! Here you can view the user's cleanup report, trigger cleanups, and securely log out.
                    </p>
                </div>
            </div>

        </>
    );
}
