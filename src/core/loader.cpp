#include <iliad.hpp>
#include <core/loader.hpp>

Iliad::Core::Loader::Loader(Iliad::Server& server) : Iliad::Loader(server) {

}

Iliad::Core::Loader::~Loader(){

}

std::string Iliad::Core::Loader::name(){
	return "Core";
}

std::map<std::string, Iliad::Package*> Iliad::Core::Loader::packages(){
	std::map<std::string, Iliad::Package*> packages;
	return packages;
}

