package com.wildboar.backend.repository;

import com.wildboar.backend.model.Detection;
import org.springframework.data.jpa.repository.JpaRepository;

public interface DetectionRepository extends JpaRepository<Detection, Long> {
}
