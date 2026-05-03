package com.registry.verg.eagent.repository;

import com.registry.verg.eagent.entity.EagentEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface EagentRepository extends JpaRepository<EagentEntity, String> {

}