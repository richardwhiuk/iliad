#include <server.hpp>

Iliad::Server::Server(){

}

Iliad::Server::~Server(){

	for(std::map<std::string, Loader*>::iterator it = loaders.begin(); it != loaders.end(); it ++){
		delete (it->second);
	}

}

void Iliad::Server::process(Iliad::Request& req, Iliad::Response& rep){

}


