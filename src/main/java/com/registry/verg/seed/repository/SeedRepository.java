package com.registry.verg.seed.repository;

import com.registry.verg.seed.entity.SeedEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface SeedRepository extends JpaRepository<SeedEntity, String> {

}