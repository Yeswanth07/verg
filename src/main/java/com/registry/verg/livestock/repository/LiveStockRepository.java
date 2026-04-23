package com.registry.verg.livestock.repository;


import com.registry.verg.livestock.entity.LiveStockEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface LiveStockRepository extends JpaRepository<LiveStockEntity, String> {

}