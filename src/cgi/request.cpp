#include <cgi/request.hpp>

Iliad::CGI::Request::Request(int argc, char** argv, std::istream& in) : Iliad::Request(){
	std::vector<std::string> args;
	for(int i = 0; i < argc; i ++){
		args.push_back(std::string(argv[i]));
	}   
	Request(args, in);
} 

Iliad::CGI::Request::Request(std::vector<std::string>& args, std::istream& in){

}

