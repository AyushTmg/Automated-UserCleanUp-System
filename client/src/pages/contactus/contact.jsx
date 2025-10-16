import React from 'react';
import Header from '../../components/Header/header';

export default function ContactUs() {
    return (
        <>
            <Header />

            <div className="container d-flex align-items-center justify-content-center min-vh-100">
                <div className="row w-100">
                    <div className="col-md-8 mx-auto">
                        <div className="">
                            <div className="card-body p-5">
                                <h2 className="card-title text-center mb-4">Contact Us</h2>
                                <p className="text-center mb-5 text-muted">
                                    We'd love to hear from you! Fill out the form below and we'll get back to you as soon as possible.
                                </p>

                                <form>
                                    <div className="mb-3">
                                        <label htmlFor="name" className="form-label">Your Name</label>
                                        <input type="text" className="form-control" id="name" placeholder="Enter your full name" required />
                                    </div>

                                    <div className="mb-3">
                                        <label htmlFor="email" className="form-label">Email address</label>
                                        <input type="email" className="form-control" id="email" placeholder="name@example.com" required />
                                    </div>

                                    <div className="mb-3">
                                        <label htmlFor="subject" className="form-label">Subject</label>
                                        <input type="text" className="form-control" id="subject" placeholder="What is this about?" />
                                    </div>

                                    <div className="mb-4">
                                        <label htmlFor="message" className="form-label">Message</label>
                                        <textarea className="form-control" id="message" rows="5" placeholder="Type your message here..." required></textarea>
                                    </div>

                                    <div className="d-grid">
                                        <button type="submit" className="btn btn-primary btn-lg">Send Message</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </>
    );
}
