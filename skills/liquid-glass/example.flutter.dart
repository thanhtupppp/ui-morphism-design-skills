import 'dart:ui';
import 'package:flutter/material.dart';

class LiquidGlassToolbar extends StatelessWidget {
  const LiquidGlassToolbar({super.key, this.effectsEnabled = true});

  final bool effectsEnabled;

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final compact = constraints.maxWidth < 600;
        final horizontalPadding = compact ? 8.0 : 12.0;
        final blur = compact ? 14.0 : 20.0;
        final toolbar = Container(
          padding: EdgeInsets.symmetric(horizontal: horizontalPadding, vertical: 8),
          decoration: BoxDecoration(
            color: effectsEnabled ? const Color(0x9EFFFFFF) : Theme.of(context).colorScheme.surface,
            border: Border.all(color: effectsEnabled ? const Color(0xB8FFFFFF) : Theme.of(context).colorScheme.outline),
            borderRadius: BorderRadius.circular(999),
          ),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              IconButton(
                tooltip: 'Search',
                onPressed: () {},
                style: IconButton.styleFrom(minimumSize: const Size(48, 48)),
                icon: const Icon(Icons.search),
              ),
              IconButton(
                tooltip: 'Settings',
                onPressed: () {},
                style: IconButton.styleFrom(minimumSize: const Size(48, 48)),
                icon: const Icon(Icons.settings),
              ),
            ],
          ),
        );

        if (!effectsEnabled) return toolbar;

        return ClipRRect(
          borderRadius: BorderRadius.circular(999),
          child: BackdropFilter(
            filter: ImageFilter.blur(sigmaX: blur, sigmaY: blur),
            child: toolbar,
          ),
        );
      },
    );
  }
}

// Verification: native IconButton semantics, LayoutBuilder responsive behavior, and 48px targets.
// Fallback: set effectsEnabled=false to retain the opaque surface, labels, order, and interaction state.
