#include <iliad.hpp>

#include <core/config/package.hpp>

Iliad::Core::Config::Package::Package(Iliad::Server& server) : Iliad::Package::Package(server) {

}

Iliad::Core::Config::Package::~Package(){

}

std::string Iliad::Core::Config::Package::name(){
	return "Config";
}

std::map<std::string, Iliad::Module*> Iliad::Core::Config::Package::modules(){
	std::map<std::string, Iliad::Module*> modules;

	return modules;
}

