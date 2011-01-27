#include <iliad.hpp>

#include <iostream>

#include <cgi/server.hpp>
#include <cgi/log.hpp>
#include <cgi/request.hpp>
#include <cgi/response.hpp>

int main(int argc, char** argv){

	#ifdef DEBUG
		std::cout << "Content-type: text/plain" << std::endl << std::endl;
	#endif

	Iliad::CGI::Log log(std::cerr);

	Iliad::CGI::Request request(argc, argv, std::cin); 

	Iliad::CGI::Response response(std::cout);

	Iliad::CGI::Server server;

	try {
		server.process(request, response);
		return 0;
	} catch(...){
		return -1;
	}

}

