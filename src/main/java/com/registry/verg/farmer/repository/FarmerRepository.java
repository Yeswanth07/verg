package com.registry.verg.farmer.repository;

import com.registry.verg.farmer.entity.FarmerEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface FarmerRepository extends JpaRepository<FarmerEntity, String> {

}